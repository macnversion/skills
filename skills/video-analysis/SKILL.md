---
name: video-analysis
description: AI-powered video content analysis capability. Use when Claude needs to analyze video files to understand their content, identify key moments, extract product features, or perform custom video analysis. Supports: (1) General content analysis, (2) Product/functionality analysis, (3) Key node identification, (4) Custom prompt analysis. Requires ARK_API_KEY environment variable for video analysis API.
---

# Video Analysis

AI-powered video content understanding capability that enables intelligent analysis of video files.

## Workflow

Using video-analysis involves these steps:

1. **Prepare environment** - Set `ARK_API_KEY` environment variable
2. **Select analysis type** - Choose from general, product, key_nodes, or custom
3. **Run analysis** - Use VideoAnalyzer with appropriate analysis type
4. **Handle results** - Parse output and handle errors

## Quick Start

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()
result = analyzer.analyze_video("path/to/video.mp4", analysis_type="general")
```

## Analysis Types

| Type | Use Case |
|------|----------|
| `general` | Quick content overview and summary |
| `product` | App/feature understanding from product perspective |
| `key_nodes` | Timestamped moments for testing/documentation |
| `custom` | Specialized analysis with your prompt |

See [Analysis Types](references/analysis-types.md) for detailed usage of each type.

## Scripts

- `video_analyzer.py` - Main VideoAnalyzer class
- `prompt_manager.py` - Prompt management for different analysis types
- `response_extractor.py` - Response parsing utilities
- `prompts/` - Prompt templates for each analysis type

See [API Reference](references/api-reference.md) for complete documentation.

## Output Format

All results return structured JSON with `analysis_result` and `metadata`.

See [Output Guide](references/output-guide.md) for quality standards and examples.

## Error Handling

Handle common errors: FileNotFoundError, ValueError, RuntimeError.

See [Error Handling](references/error-handling.md) for detailed troubleshooting.

## Configuration

Set environment variable:
```bash
export ARK_API_KEY="your_api_key_here"
```

Optional: Override in VideoAnalyzer constructor with `api_key`, `base_url`, or `model` parameters.
