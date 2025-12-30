# Output Guide

Quality standards and examples for video analysis output.

## Output Structure

All analysis results follow this structure:

```json
{
  "analysis_result": {
    // Analysis-specific content
  },
  "metadata": {
    "video_path": "/path/to/video.mp4",
    "video_filename": "video.mp4",
    "video_info": {
      "filename": "video.mp4",
      "size_mb": 15.5
    },
    "analysis_type": "general",
    "analysis_time": "2025-12-29T10:30:00"
  }
}
```

---

## Quality Standards

### General Content Analysis

**Required fields:**

```json
{
  "overview": "Brief 1-2 sentence description of video content",
  "key_elements": ["List of main objects/people visible"],
  "actions": ["List of actions or activities in video"],
  "summary": "Comprehensive 2-3 paragraph summary"
}
```

**Quality checklist:**

- [ ] Overview captures main subject and setting
- [ ] Key elements list is comprehensive (5-10 items)
- [ ] Actions describe what happens in order
- [ ] Summary provides complete context

**Good example:**

```json
{
  "overview": "A software developer demonstrating a new feature on a laptop in an office setting",
  "key_elements": ["Developer at desk", "Laptop with code editor", "Coffee cup", "Office whiteboard", "Developer wearing headphones"],
  "actions": [
    "Developer types code into editor",
    "Switches to browser window",
    "Clicks through application interface",
    "Points at screen while explaining"
  ],
  "summary": "This video features a software developer demonstrating a new dashboard feature in what appears to be an internal product. The developer starts by showing the code implementation in a dark-themed editor, then switches to a live browser demo where they navigate through several screens explaining the new analytics widgets. Throughout the demo, the developer frequently points at the screen to highlight specific UI elements and pauses occasionally to speak directly to the camera. The setting suggests an office environment with a whiteboard visible in the background and typical office items like a coffee cup on the desk."
}
```

**Bad example:**

```json
{
  "overview": "A guy showing something on his computer",
  "key_elements": ["Computer", "Person"],
  "actions": ["Using computer"],
  "summary": "The video shows someone using a computer."
}
```

---

### Product/Functionality Analysis

**Required fields:**

```json
{
  "product_name": "Name of product or feature",
  "main_function": "Primary purpose of the product",
  "user_flow": ["Step-by-step user journey"],
  "key_features": ["List of demonstrated features"]
}
```

**Quality checklist:**

- [ ] Product name is identified correctly
- [ ] Main function is clearly stated
- [ ] User flow has 3-8 steps
- [ ] Key features are comprehensive

**Good example:**

```json
{
  "product_name": "TaskFlow - Project Management Dashboard",
  "main_function": "Team collaboration and project tracking tool",
  "user_flow": [
    "User logs in to dashboard",
    "Navigates to Projects tab",
    "Creates new project with template",
    "Adds team members to project",
    "Creates and assigns tasks",
    "Views progress in analytics view"
  ],
  "key_features": [
    "Kanban board view for task management",
    "Real-time team collaboration indicators",
    "Pre-built project templates",
    "Interactive analytics dashboard",
    "Email notifications for task updates",
    "Drag-and-drop task organization"
  ]
}
```

---

### Key Node Identification

**Required fields:**

```json
{
  "key_nodes": [
    {
      "timestamp": "MM:SS or HH:MM:SS",
      "description": "Clear description of the moment",
      "importance": "high|medium|low",
      "type": "action|transition|event|feature"
    }
  ]
}
```

**Quality checklist:**

- [ ] Timestamps are accurate
- [ ] Descriptions are clear and specific
- [ ] Importance levels are appropriate
- [ ] Node types are correctly categorized
- [ ] 5-15 key nodes for typical video

**Good example:**

```json
{
  "key_nodes": [
    {
      "timestamp": "00:00:15",
      "description": "Login screen appears with email and password fields",
      "importance": "high",
      "type": "feature"
    },
    {
      "timestamp": "00:00:42",
      "description": "User successfully logs in, dashboard loads",
      "importance": "high",
      "type": "action"
    },
    {
      "timestamp": "00:01:23",
      "description": "User clicks 'New Project' button in top navigation",
      "importance": "medium",
      "type": "action"
    },
    {
      "timestamp": "00:01:45",
      "description": "Project template selection modal appears",
      "importance": "high",
      "type": "feature"
    },
    {
      "timestamp": "00:02:30",
      "description": "User drags task card to 'In Progress' column",
      "importance": "medium",
      "type": "action"
    },
    {
      "timestamp": "00:03:15",
      "description": "Notification bell icon pulses with new notification",
      "importance": "low",
      "type": "feature"
    }
  ]
}
```

**Bad example:**

```json
{
  "key_nodes": [
    {"timestamp": "0:15", "description": "Login", "importance": "high", "type": "event"},
    {"timestamp": "1:00", "description": "Dashboard", "importance": "high", "type": "event"},
    {"timestamp": "2:00", "description": "Something happens", "importance": "medium", "type": "event"}
  ]
}
```

---

## Custom Prompt Output

When using custom prompts, ensure the output:

1. **Follows requested format** (JSON, markdown, etc.)
2. **Addresses all requested criteria**
3. **Provides sufficient detail**
4. **Uses consistent structure**

**Example custom prompt with structured output:**

Prompt:
```
Analyze this video for accessibility issues.
Return in JSON format:
{
  "contrast_issues": [],
  "navigation_problems": [],
  "text_readability": "",
  "recommendations": []
}
```

**Good output:**

```json
{
  "contrast_issues": [
    "Light gray text (#AAAAAA) on white background fails WCAG AA",
    "Submit button color (#4A90D9) has insufficient contrast against page background"
  ],
  "navigation_problems": [
    "No keyboard focus indicators on interactive elements",
    "Skip navigation link missing",
    "Form fields lack proper labels"
  ],
  "text_readability": "Most text is 14px sans-serif, which is readable. However, some caption text appears at 12px and could be difficult for some users to read.",
  "recommendations": [
    "Increase text contrast ratio to at least 4.5:1",
    "Add visible focus indicators (2px outline)",
    "Add skip link as first page element",
    "Increase caption text size to 14px minimum"
  ]
}
```

---

## Metadata Standards

Always include complete metadata:

```json
{
  "metadata": {
    "video_path": "/absolute/path/to/video.mp4",
    "video_filename": "video.mp4",
    "video_info": {
      "filename": "video.mp4",
      "size_mb": 15.5,
      "duration_seconds": 180
    },
    "analysis_type": "general",
    "analysis_time": "2025-12-29T10:30:00",
    "model_used": "model-name",
    "api_version": "v1"
  }
}
```

---

## Error Responses

When analysis fails, return structured error:

```json
{
  "error": "Human-readable error message",
  "error_type": "FileNotFoundError|ValueError|RuntimeError",
  "metadata": {
    "video_path": "/path/to/video.mp4",
    "analysis_type": "general",
    "analysis_time": "2025-12-29T10:30:00"
  }
}
```

---

## Output Validation

Before returning results, verify:

1. **All required fields present**
2. **No null or undefined values**
3. **Correct data types** (string, array, object)
4. **Reasonable content length** (not empty, not excessively long)
5. **Valid JSON format** (if JSON output requested)

```python
def validate_output(result, analysis_type):
    if "error" in result:
        return True  # Error responses are valid
    
    if "analysis_result" not in result:
        return False
    
    if "metadata" not in result:
        return False
    
    # Type-specific validation
    if analysis_type == "general":
        required = ["overview", "key_elements", "actions", "summary"]
    elif analysis_type == "product":
        required = ["product_name", "main_function", "user_flow", "key_features"]
    elif analysis_type == "key_nodes":
        required = ["key_nodes"]
    
    for field in required:
        if field not in result["analysis_result"]:
            return False
    
    return True
```
