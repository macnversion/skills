#!/usr/bin/env python3
"""
Example usage of the video-analysis skill

This script demonstrates how to use the VideoAnalyzer class
for different types of video analysis.
"""

import sys
import json
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / "scripts"))

from video_analyzer import VideoAnalyzer


def example_general_analysis(video_path: str):
    """Example 1: General content analysis"""
    print("=" * 60)
    print("Example 1: General Content Analysis")
    print("=" * 60)

    analyzer = VideoAnalyzer()
    result = analyzer.analyze_video(video_path, analysis_type="general")

    print("\nResult:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def example_product_analysis(video_path: str):
    """Example 2: Product functionality analysis"""
    print("\n" + "=" * 60)
    print("Example 2: Product Functionality Analysis")
    print("=" * 60)

    analyzer = VideoAnalyzer()
    result = analyzer.analyze_video(video_path, analysis_type="product")

    print("\nResult:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def example_key_nodes(video_path: str):
    """Example 3: Key node identification"""
    print("\n" + "=" * 60)
    print("Example 3: Key Node Identification")
    print("=" * 60)

    analyzer = VideoAnalyzer()
    result = analyzer.analyze_video(video_path, analysis_type="key_nodes")

    print("\nResult:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def example_custom_analysis(video_path: str):
    """Example 4: Custom prompt analysis"""
    print("\n" + "=" * 60)
    print("Example 4: Custom Prompt Analysis")
    print("=" * 60)

    custom_prompt = """
    Analyze this video and identify:
    1. What user interface elements are shown?
    2. Are there any accessibility issues?
    3. What is the overall user experience like?

    Return your analysis in JSON format.
    """

    analyzer = VideoAnalyzer()
    result = analyzer.analyze_with_prompt(video_path, custom_prompt)

    print("\nResult:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    """Run all examples"""
    if len(sys.argv) < 2:
        print("Usage: python example_usage.py <video_path>")
        print("\nThis script demonstrates different analysis types:")
        print("  1. General content analysis")
        print("  2. Product functionality analysis")
        print("  3. Key node identification")
        print("  4. Custom prompt analysis")
        print("\nMake sure to set ARK_API_KEY environment variable:")
        print("  export ARK_API_KEY='your_api_key'")
        sys.exit(1)

    video_path = sys.argv[1]

    if not Path(video_path).exists():
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)

    # Run examples
    try:
        example_general_analysis(video_path)
        # Uncomment to run other examples:
        # example_product_analysis(video_path)
        # example_key_nodes(video_path)
        # example_custom_analysis(video_path)

        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)

    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()