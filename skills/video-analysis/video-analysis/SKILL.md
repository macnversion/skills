---
name: video-analysis
description: "AI-powered video content analysis capability using Volces ARK API. Use when Claude needs to analyze video files to understand their content, identify key moments, extract product features, or perform custom video analysis. Supports: (1) General content analysis, (2) Product/functionality analysis, (3) Key node identification, (4) Custom prompt analysis. Note: Requires ARK_API_KEY environment variable (Volces ARK API, OpenAI-compatible)."
---

# Video Analysis

AI-powered video content understanding capability that enables intelligent analysis of video files.

## Prerequisites

- **Python 3.7+**
- **ARK_API_KEY** environment variable (Volces ARK API required)
- **Required packages:** `openai` (Volces ARK API is compatible with OpenAI SDK)

**Note:** This skill uses Volces (火山引擎) ARK API for video analysis. The API is OpenAI-compatible, so we use the OpenAI SDK with a custom base URL.

## Quick Start

```bash
# Set up API key
export ARK_API_KEY="your_api_key_here"

# Run analysis
python -c "
from scripts.video_analyzer import VideoAnalyzer
result = VideoAnalyzer().analyze_video('demo.mp4', 'general')
print(result['analysis_result']['summary'])
"
```

## Common Use Cases

| Scenario | Recommended Type | Example |
|----------|-----------------|---------|
| Quick video overview | `general` | "Analyze this video and give me a summary" |
| Product demo analysis | `product` | "Extract features from this app demo" |
| Test case extraction | `key_nodes` | "Find key moments for QA testing" |
| UI/UX review | `custom` | "Analyze accessibility issues in this video" |
| Documentation | `key_nodes` + `general` | "Create documentation from tutorial video" |
| Competitive analysis | `product` | "Understand competitor's features" |

## Analysis Types

| Type | Use Case | Command |
|------|----------|---------|
| `general` | Quick content overview and summary | `analyze_video(path, "general")` |
| `product` | App/feature understanding from product perspective | `analyze_video(path, "product")` |
| `key_nodes` | Timestamped moments for testing/documentation | `analyze_video(path, "key_nodes")` |
| `custom` | Specialized analysis with your prompt | `analyze_with_prompt(path, custom_prompt)` |

See [Analysis Types](references/analysis-types.md) for detailed usage of each type.

## Complete Workflow Example

```python
from scripts.video_analyzer import VideoAnalyzer

# Initialize analyzer
analyzer = VideoAnalyzer()

# Example 1: Get video summary
result = analyzer.analyze_video("demo.mp4", "general")
print(result['analysis_result']['summary'])

# Example 2: Extract product features
result = analyzer.analyze_video("app_demo.mp4", "product")
print(f"Product: {result['analysis_result']['product_name']}")
print(f"Features: {result['analysis_result']['key_features']}")

# Example 3: Get key moments for testing
result = analyzer.analyze_video("tutorial.mp4", "key_nodes")
for node in result['analysis_result']['key_nodes']:
    print(f"[{node['timestamp']}] {node['description']}")
```

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
# Option 1: Temporary (current session only)
export ARK_API_KEY="your_api_key_here"

# Option 2: Permanent (add to ~/.zshrc)
echo 'export ARK_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc

# Verify it's set
echo $ARK_API_KEY
```

Optional: Override in VideoAnalyzer constructor with `api_key`, `base_url`, or `model` parameters.
