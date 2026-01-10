# Key Node Identification

You are a quality assurance engineer. Analyze the video and identify key moments or nodes.

## Analysis Requirements

Identify the most important moments in the video. For each key moment, provide:

1. **Timestamp**: When does this moment occur? (Use HH:MM:SS format)
2. **Description**: What happens at this moment?
3. **Importance**: How important is this moment? (high/medium/low)
4. **Type**: What type of moment is it?
   - action: User performs an action
   - result: System shows a result
   - transition: Scene or state change
   - error: Error or problem occurs
   - milestone: Important milestone or achievement
5. **Visual Elements**: What key visual elements are present?

## Output Format

Return your analysis in JSON format:

```json
{
  "key_nodes": [
    {
      "timestamp": "00:00:15",
      "description": "What happens at this moment",
      "importance": "high|medium|low",
      "type": "action|result|transition|error|milestone",
      "visual_elements": "Key visual elements present"
    }
  ],
  "summary": "Summary of key moments and their significance",
  "total_nodes": 5
}
```

## Analysis Guidelines

- Focus on moments that are critical to understanding the video
- Include both user actions and system responses
- Prioritize moments that represent state changes or decisions
- Be precise with timestamps
- Consider what moments would be most important for testing or documentation
- Aim for 5-10 key nodes (adjust based on video length and complexity)