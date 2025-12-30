#!/usr/bin/env python3
"""
Prompt Manager - Manages analysis prompts for video analysis
"""

from pathlib import Path
from typing import Dict, Any


class PromptManager:
    """Manages video analysis prompts"""

    def __init__(self):
        # Get prompts directory relative to this script
        script_dir = Path(__file__).parent
        self.prompts_dir = script_dir / "prompts"

    def _load_prompt_template(self, template_name: str) -> str:
        """Load prompt template from file"""
        prompt_file = self.prompts_dir / f"{template_name}.md"
        if prompt_file.exists():
            return prompt_file.read_text(encoding='utf-8')
        return ""

    def get_general_analysis_prompt(self, video_info: Dict[str, Any] = None) -> str:
        """Get general video analysis prompt"""
        template = self._load_prompt_template("general_analysis")

        if not template:
            # Fallback to built-in prompt
            template = """Analyze this video and provide a comprehensive summary.

Please provide:
1. **Content Overview**: What does the video show?
2. **Key Elements**: Main objects, people, or features visible
3. **Actions**: What actions or movements occur?
4. **Context**: What's the purpose or scenario?
5. **Summary**: Brief summary of the entire video

Return your analysis in JSON format:
{
    "overview": "Brief overview",
    "key_elements": ["element1", "element2"],
    "actions": ["action1", "action2"],
    "context": "Context description",
    "summary": "Full summary"
}"""

        # Add video info if available
        if video_info:
            template += f"\n\nVideo Information:\n"
            template += f"- Filename: {video_info.get('filename', 'unknown')}\n"
            template += f"- Size: {video_info.get('size_mb', 0)} MB\n"

        return template

    def get_product_analysis_prompt(self, video_info: Dict[str, Any] = None) -> str:
        """Get product/functionality analysis prompt"""
        template = self._load_prompt_template("product_analysis")

        if not template:
            # Fallback to built-in prompt
            template = """Analyze this video as a product manager would analyze an app or feature.

Please provide:
1. **Product Name**: What product or feature is shown?
2. **Main Function**: What is the primary function?
3. **User Flow**: What are the main steps users take?
4. **Key Features**: What features are demonstrated?
5. **User Experience**: How does the user interact with it?

Return your analysis in JSON format:
{
    "product_name": "Name",
    "main_function": "Description",
    "user_flow": ["step1", "step2", "step3"],
    "key_features": ["feature1", "feature2"],
    "user_experience": "Description"
}"""

        # Add video info if available
        if video_info:
            template += f"\n\nVideo Information:\n"
            template += f"- Filename: {video_info.get('filename', 'unknown')}\n"
            template += f"- Size: {video_info.get('size_mb', 0)} MB\n"

        return template

    def get_key_nodes_prompt(self, video_info: Dict[str, Any] = None) -> str:
        """Get key node identification prompt"""
        template = self._load_prompt_template("key_nodes")

        if not template:
            # Fallback to built-in prompt
            template = """Analyze this video and identify key moments or nodes.

For each key moment, provide:
1. **Timestamp**: When does it occur (HH:MM:SS format)?
2. **Description**: What happens at this moment?
3. **Importance**: How important is this moment? (high/medium/low)
4. **Type**: What type of moment is it? (action, result, transition, etc.)

Return your analysis in JSON format:
{
    "key_nodes": [
        {
            "timestamp": "00:00:15",
            "description": "What happens",
            "importance": "high",
            "type": "action"
        }
    ],
    "summary": "Summary of key moments"
}"""

        # Add video info if available
        if video_info:
            template += f"\n\nVideo Information:\n"
            template += f"- Filename: {video_info.get('filename', 'unknown')}\n"
            template += f"- Size: {video_info.get('size_mb', 0)} MB\n"

        return template