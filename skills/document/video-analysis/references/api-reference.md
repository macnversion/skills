# API Reference

Complete documentation for the video analysis scripts.

## VideoAnalyzer

Main analyzer class for video content analysis.

### Constructor

```python
VideoAnalyzer(api_key=None, base_url=None, model=None)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `api_key` | string | No | Override ARK_API_KEY environment variable |
| `base_url` | string | No | Custom API endpoint URL |
| `model` | string | No | Custom model name for analysis |

**Example:**

```python
# Use environment variable (recommended)
analyzer = VideoAnalyzer()

# Override with custom values
analyzer = VideoAnalyzer(
    api_key="custom_api_key",
    base_url="https://custom-api.example.com",
    model="custom-model-name"
)
```

---

### analyze_video()

Analyze a video file with the specified analysis type.

```python
analyzer.analyze_video(video_path, analysis_type)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_path` | string | Yes | Path to video file |
| `analysis_type` | string | Yes | Type of analysis: `general`, `product`, `key_nodes`, `custom` |

**Returns:** Dictionary with `analysis_result` and `metadata`

**Example:**

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()
result = analyzer.analyze_video("path/to/video.mp4", analysis_type="general")

print(result)
# {
#   "analysis_result": {...},
#   "metadata": {
#     "video_path": "/path/to/video.mp4",
#     "video_filename": "video.mp4",
#     "video_info": {"filename": "video.mp4", "size_mb": 15.5},
#     "analysis_type": "general",
#     "analysis_time": "2025-12-29T10:30:00"
#   }
# }
```

**Error Handling:**

```python
try:
    result = analyzer.analyze_video("video.mp4", "general")
    if "error" in result:
        print(f"Analysis error: {result['error']}")
    else:
        print(result['analysis_result'])
except FileNotFoundError:
    print("Video file not found")
except ValueError as e:
    print(f"Invalid input: {e}")
except RuntimeError as e:
    print(f"Runtime error: {e}")
```

---

### analyze_with_prompt()

Analyze a video using a custom prompt.

```python
analyzer.analyze_with_prompt(video_path, prompt)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_path` | string | Yes | Path to video file |
| `prompt` | string | Yes | Custom analysis prompt |

**Returns:** Dictionary with custom analysis results

**Example:**

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()

custom_prompt = """
Analyze this video and identify:
1. Main subject(s)
2. Actions performed
3. Setting/location
4. Overall mood/tone

Return results as a structured summary.
"""

result = analyzer.analyze_with_prompt("video.mp4", custom_prompt)
print(result)
```

---

## PromptManager

Manages analysis prompts for different analysis types.

### Constructor

```python
PromptManager()
```

No parameters required. Loads prompt templates from `scripts/prompts/` directory.

---

### get_general_analysis_prompt()

Generate prompt for general content analysis.

```python
prompt_manager.get_general_analysis_prompt(video_info)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_info` | dict | Yes | Video information dictionary |

**Returns:** Prompt string for general analysis

---

### get_product_analysis_prompt()

Generate prompt for product/functionality analysis.

```python
prompt_manager.get_product_analysis_prompt(video_info)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_info` | dict | Yes | Video information dictionary |

**Returns:** Prompt string for product analysis

---

### get_key_nodes_prompt()

Generate prompt for key node identification.

```python
prompt_manager.get_key_nodes_prompt(video_info)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_info` | dict | Yes | Video information dictionary |

**Returns:** Prompt string for key nodes analysis

---

### get_custom_analysis_prompt()

Generate prompt for custom analysis.

```python
prompt_manager.get_custom_analysis_prompt(video_info, custom_prompt)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `video_info` | dict | Yes | Video information dictionary |
| `custom_prompt` | string | Yes | User's custom prompt |

**Returns:** Prompt string for custom analysis

---

### _load_prompt_template()

Load a prompt template from file.

```python
prompt_manager._load_prompt_template(template_name)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `template_name` | string | Yes | Name of template file (without .md) |

**Returns:** Template string content

---

## ResponseExtractor

Utilities for extracting text from API responses.

### extract_text_from_response()

Universal response parser that handles various API response formats.

```python
extract_text_from_response(response)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `response` | dict | Yes | API response dictionary |

**Returns:** Extracted text string

**Example:**

```python
from scripts.response_extractor import extract_text_from_response

api_response = {
    "choices": [
        {"message": {"content": "Analysis result text"}}
    ]
}

text = extract_text_from_response(api_response)
print(text)  # "Analysis result text"
```

---

## Prompt Templates

Located in `scripts/prompts/` directory:

### general_analysis.md

Template for general content analysis. Returns overview, key elements, actions, and summary.

### product_analysis.md

Template for product/functionality analysis. Returns product name, main function, user flow, and key features.

### key_nodes.md

Template for key node identification. Returns timestamped key moments with descriptions and importance levels.

### Custom Templates

To add custom prompts:

1. Create new `.md` file in `scripts/prompts/`
2. Add prompt template with analysis instructions
3. Use with `analyze_with_prompt()` method

**Example custom prompt template:**

```markdown
# Custom Analysis

Analyze this video for specific criteria:

## Criteria
1. [Your criteria 1]
2. [Your criteria 2]
3. [Your criteria 3]

## Output Format
Return JSON:
{
  "finding_1": "description",
  "finding_2": "description",
  "finding_3": "description"
}
```

---

## Video Requirements

### Supported Formats

- `.mp4` (recommended)
- `.mov`
- `.avi`
- `.mkv`

### Size Limits

- **Maximum size:** 500MB (configurable)
- **Recommended:** Under 100MB for faster processing

### Best Practices

1. Use MP4 format for best compatibility
2. Compress large videos before analysis
3. Ensure clear audio for speech analysis
4. Good lighting improves visual analysis quality

---

## Environment Variables

### ARK_API_KEY (Required)

API key for video analysis service.

```bash
export ARK_API_KEY="your_api_key_here"
```

### Optional Configuration

| Variable | Description |
|----------|-------------|
| `ARK_BASE_URL` | Custom API endpoint (overridden by constructor) |
| `ARK_MODEL` | Custom model name (overridden by constructor) |
