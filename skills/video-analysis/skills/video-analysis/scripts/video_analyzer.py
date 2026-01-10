#!/usr/bin/env python3
"""
Video Analyzer - Core video analysis functionality

This module provides the main video analysis capabilities including:
- Video upload to API
- Content analysis with AI
- Key node identification
- Custom prompt analysis
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, List

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from prompt_manager import PromptManager
from response_extractor import extract_text_from_response


class VideoAnalyzer:
    """Video analyzer for AI-powered video content understanding"""

    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        """
        Initialize video analyzer

        Args:
            api_key: API key for video analysis service (defaults to ARK_API_KEY env var)
            base_url: Base URL for API (defaults to Volces ARK)
            model: Model name to use for analysis
        """
        if OpenAI is None:
            raise RuntimeError("openai package is required. Install with: pip install openai")

        self.api_key = api_key or os.getenv('ARK_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required. Set ARK_API_KEY environment variable or pass api_key parameter")

        self.base_url = base_url or "https://ark.cn-beijing.volces.com/api/v3"
        self.model = model or "ep-20250912105916-n6xlt"
        self.temperature = 0.1

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )
        self.prompt_manager = PromptManager()

    def analyze_video(self, video_path: str,
                     analysis_type: str = "general",
                     custom_prompt: str = None) -> Dict[str, Any]:
        """
        Analyze video content

        Args:
            video_path: Path to video file
            analysis_type: Type of analysis
                - "general": General content analysis
                - "product": Product/functionality analysis
                - "key_nodes": Key node identification
                - "custom": Use custom_prompt
            custom_prompt: Custom prompt for analysis (required when analysis_type="custom")

        Returns:
            Dict containing analysis results
        """
        # Validate inputs
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")

        if analysis_type == "custom" and not custom_prompt:
            raise ValueError("custom_prompt is required when analysis_type='custom'")

        print(f"Analyzing video: {os.path.basename(video_path)}")

        # Upload video
        file_id = self._upload_video(video_path)

        # Get video info
        video_info = self._get_video_info(video_path)

        # Get prompt based on analysis type
        if analysis_type == "general":
            prompt = self.prompt_manager.get_general_analysis_prompt(video_info)
        elif analysis_type == "product":
            prompt = self.prompt_manager.get_product_analysis_prompt(video_info)
        elif analysis_type == "key_nodes":
            prompt = self.prompt_manager.get_key_nodes_prompt(video_info)
        elif analysis_type == "custom":
            prompt = custom_prompt
        else:
            raise ValueError(f"Unknown analysis_type: {analysis_type}")

        # Perform analysis
        result = self._call_ai_analysis(file_id, prompt, f"{analysis_type} analysis")

        # Add metadata
        result['metadata'] = {
            'video_path': video_path,
            'video_filename': os.path.basename(video_path),
            'video_info': video_info,
            'analysis_type': analysis_type,
            'analysis_time': datetime.now().isoformat()
        }

        return result

    def analyze_with_prompt(self, video_path: str, prompt: str) -> Dict[str, Any]:
        """
        Analyze video with custom prompt

        Args:
            video_path: Path to video file
            prompt: Custom analysis prompt

        Returns:
            Dict containing analysis results
        """
        return self.analyze_video(video_path, analysis_type="custom", custom_prompt=prompt)

    def _upload_video(self, video_path: str) -> str:
        """Upload video to API and return file ID"""
        print("Uploading video file...")
        with open(video_path, "rb") as video_file:
            file = self.client.files.create(
                file=video_file,
                purpose="user_data"
            )

        print(f"Video uploaded: {file.id}")

        # Wait for processing
        while file.status == "processing":
            time.sleep(2)
            file = self.client.files.retrieve(file.id)

        print(f"Video processing complete: {file.status}")
        return file.id

    def _get_video_info(self, video_path: str) -> Dict[str, Any]:
        """Get basic video information"""
        file_stat = os.stat(video_path)
        return {
            'filename': os.path.basename(video_path),
            'filepath': video_path,
            'size': file_stat.st_size,
            'size_mb': round(file_stat.st_size / 1024 / 1024, 2)
        }

    def _call_ai_analysis(self, file_id: str, prompt: str, stage_name: str) -> Dict[str, Any]:
        """Call AI analysis API"""
        max_retries = 3
        last_error = None

        for attempt in range(max_retries):
            try:
                response = self.client.responses.create(
                    model=self.model,
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "input_video",
                                    "file_id": file_id,
                                },
                                {
                                    "type": "input_text",
                                    "text": prompt,
                                },
                            ]
                        }
                    ],
                    temperature=self.temperature
                )

                content = extract_text_from_response(response)
                if not content:
                    return {"error": f"{stage_name}: API returned no content"}

                # Try to parse as JSON
                try:
                    parsed = json.loads(content)
                    return parsed
                except json.JSONDecodeError:
                    # Return raw text if not JSON
                    return {"content": content}

            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    time.sleep(min(2 ** attempt, 8))
                    continue
                break

        return {"error": f"{stage_name}: API call failed - {str(last_error)}"}


def main():
    """Example usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python video_analyzer.py <video_path> [analysis_type]")
        print("  analysis_type: general, product, key_nodes, custom")
        sys.exit(1)

    video_path = sys.argv[1]
    analysis_type = sys.argv[2] if len(sys.argv) > 2 else "general"

    analyzer = VideoAnalyzer()
    result = analyzer.analyze_video(video_path, analysis_type)

    print("\nAnalysis Result:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()