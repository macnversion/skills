# Analysis Types

Detailed usage guide for each analysis type.

## Quick Decision Guide

| 你的需求 | 推荐类型 | 命令 |
|---------|---------|------|
| 快速了解视频内容 | `general` | `analyzer.analyze_video(path, "general")` |
| 分析产品功能 | `product` | `analyzer.analyze_video(path, "product")` |
| 提取关键时间点 | `key_nodes` | `analyzer.analyze_video(path, "key_nodes")` |
| 自定义分析 | `custom` | `analyzer.analyze_with_prompt(path, prompt)` |

## Contents

- [1. General Content Analysis](#1-general-content-analysis) - Quick video overview and summary
- [2. Product/Functionality Analysis](#2-productfunctionality-analysis) - Product features and user flows
- [3. Key Node Identification](#3-key-node-identification) - Timestamped key moments
- [4. Custom Prompt Analysis](#4-custom-prompt-analysis) - Specialized analysis
- [Choosing the Right Analysis Type](#choosing-the-right-analysis-type) - Decision guide
- [Combining Analysis Types](#combining-analysis-types) - Advanced usage

---

## 1. General Content Analysis

Understand the overall content of a video including main subjects, actions, and context.

### Usage

```python
result = analyzer.analyze_video("demo.mp4", analysis_type="general")
```

### Output Structure

```json
{
  "analysis_result": {
    "overview": "Brief description of video content",
    "key_elements": ["Main objects/people in video"],
    "actions": ["Actions that occur in video"],
    "summary": "Comprehensive summary of the video"
  }
}
```

### When to Use

- Need a general understanding of video content
- Summarizing video for documentation
- Quick content overview
- Initial exploration of unknown video content

### Example

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()
result = analyzer.analyze_video("demo.mp4", analysis_type="general")

if "error" in result:
    print(f"Analysis failed: {result['error']}")
else:
    print(f"Overview: {result['analysis_result']['overview']}")
    print(f"Summary: {result['analysis_result']['summary']}")
```

---

## 2. Product/Functionality Analysis

Analyze videos from a product management perspective to understand features and user flows.

### Usage

```python
result = analyzer.analyze_video("app_demo.mp4", analysis_type="product")
```

### Output Structure

```json
{
  "analysis_result": {
    "product_name": "Name of product or feature",
    "main_function": "Primary function of the product",
    "user_flow": ["Step-by-step user journey"],
    "key_features": ["List of demonstrated features"]
  }
}
```

### When to Use

- Analyzing app demos or feature showcases
- Understanding product functionality
- Creating product documentation
- Competitive analysis
- Preparing product reviews

### Example

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()
result = analyzer.analyze_video("app_demo.mp4", analysis_type="product")

if "error" in result:
    print(f"Analysis failed: {result['error']}")
else:
    print(f"Product: {result['analysis_result']['product_name']}")
    print(f"Main Function: {result['analysis_result']['main_function']}")
    print(f"Key Features: {result['analysis_result']['key_features']}")
```

---

## 3. Key Node Identification

Identify and timestamp important moments in a video for testing or documentation purposes.

### Usage

```python
result = analyzer.analyze_video("tutorial.mp4", analysis_type="key_nodes")
```

### Output Structure

```json
{
  "analysis_result": {
    "key_nodes": [
      {
        "timestamp": "00:02:15",
        "description": "Description of the moment",
        "importance": "high|medium|low",
        "type": "action|transition|event"
      }
    ]
  }
}
```

### When to Use

- Creating test cases from video recordings
- Documenting important moments
- Video indexing and navigation
- Quality assurance workflows
- Tutorial video bookmarking
- User guide creation

### Example

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()
result = analyzer.analyze_video("tutorial.mp4", analysis_type="key_nodes")

if "error" in result:
    print(f"Analysis failed: {result['error']}")
else:
    for node in result['analysis_result']['key_nodes']:
        print(f"[{node['timestamp']}] {node['description']} ({node['importance']})")
```

---

## 4. Custom Prompt Analysis

Use your own custom prompt for specialized analysis needs.

### Usage

```python
custom_prompt = """
Analyze this video and identify:
1. All user interface elements shown
2. Any accessibility issues
3. Color contrast problems
"""

result = analyzer.analyze_with_prompt("ux_review.mp4", custom_prompt)
```

### When to Use

- Specialized analysis requirements
- Domain-specific video understanding
- Custom evaluation criteria
- Research and data extraction
- Accessibility audits
- UI/UX reviews

### Best Practices for Custom Prompts

1. **Be specific** - Clearly define what you're looking for
2. **Request structure** - Ask for JSON output for easier parsing
3. **Include examples** - Show the desired output format
4. **Define scope** - Specify what to include and exclude
5. **Set priorities** - Indicate what's most important

### Example

```python
from scripts.video_analyzer import VideoAnalyzer

custom_prompt = """
Analyze this video for educational content quality:

1. Identify main learning objectives
2. Assess clarity of explanations
3. Note visual aids and their effectiveness
4. Suggest improvements

Return in JSON format with these fields:
{
  "learning_objectives": [],
  "explanation_clarity": "rating 1-5",
  "visual_aids_effectiveness": "rating 1-5",
  "improvements": []
}
"""

analyzer = VideoAnalyzer()
result = analyzer.analyze_with_prompt("lecture.mp4", custom_prompt)
```

---

## Choosing the Right Analysis Type

| Goal | Recommended Type |
|------|------------------|
| Quick overview | `general` |
| Understand app features | `product` |
| Create timestamps for testing | `key_nodes` |
| Extract specific data | `custom` |
| Document user flows | `product` |
| Index video content | `key_nodes` + `general` |

## Combining Analysis Types

For complex requirements, chain multiple analyses:

```python
from scripts.video_analyzer import VideoAnalyzer

analyzer = VideoAnalyzer()

# First get general overview
general_result = analyzer.analyze_video("video.mp4", analysis_type="general")

# Then get key moments for important sections
key_nodes_result = analyzer.analyze_video("video.mp4", analysis_type="key_nodes")

# Combine results for comprehensive understanding
combined = {
    "overview": general_result['analysis_result'],
    "key_moments": key_nodes_result['analysis_result']['key_nodes']
}
```
