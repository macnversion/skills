# Error Handling

Common errors and troubleshooting guide for video analysis.

## Error Types

### FileNotFoundError

Video file does not exist at the specified path.

**Cause:** Incorrect file path or file has been moved/deleted.

**Example:**

```python
try:
    result = analyzer.analyze_video("nonexistent.mp4", "general")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

**Solutions:**

1. Verify the file path is correct
2. Check if file exists:
   ```bash
   ls -la path/to/video.mp4
   ```
3. Use absolute path instead of relative path
4. Ensure file has proper read permissions

---

### ValueError

Invalid parameters or missing required configuration.

**Causes:**

- Empty video path
- Invalid analysis type
- Missing API key
- Invalid configuration parameters

**Example:**

```python
try:
    result = analyzer.analyze_video("video.mp4", "invalid_type")
except ValueError as e:
    print(f"Invalid input: {e}")
```

**Solutions:**

1. Use valid analysis types: `general`, `product`, `key_nodes`, `custom`
2. Ensure `ARK_API_KEY` is set
3. Check parameter types and formats

---

### RuntimeError

Missing dependencies or runtime configuration issues.

**Causes:**

- Missing required packages
- API connection failures
- Video upload failures

**Example:**

```python
try:
    result = analyzer.analyze_video("video.mp4", "general")
except RuntimeError as e:
    print(f"Runtime error: {e}")
```

**Solutions:**

1. Install required dependencies:
   ```bash
   pip install openai
   ```

2. Verify API key is valid:
   ```bash
   echo $ARK_API_KEY
   ```

3. Check internet connection

---

## API Key Issues

### Symptom: Authentication Errors

**Error Message:**
```
ValueError: Missing ARK_API_KEY environment variable
```

**Or:**
```
401 Unauthorized - Invalid API key
```

**Solutions:**

1. **Verify API key is set:**
   ```bash
   echo $ARK_API_KEY
   ```

2. **Set API key if not set:**
   ```bash
   export ARK_API_KEY="your_api_key_here"
   ```

3. **Add to shell profile (persistent):**
   ```bash
   echo 'export ARK_API_KEY="your_api_key_here"' >> ~/.zshrc
   source ~/.zshrc
   ```

4. **Verify API key validity:**
   ```bash
   curl -H "Authorization: Bearer $ARK_API_KEY" https://api.example.com/health
   ```

---

## Import Errors

### Symptom: Module Not Found

**Error Message:**
```
ModuleNotFoundError: No module named 'openai'
```

**Solutions:**

1. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install specific package:**
   ```bash
   pip install openai
   ```

3. **Verify Python path:**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:./scripts"
   ```

4. **Run from correct directory:**
   ```bash
   cd skills/video-analysis
   python your_script.py
   ```

---

## Video Upload Failures

### Symptom: Upload Errors

**Error Message:**
```
RuntimeError: Video upload failed
```

**Causes:**

1. Unsupported video format
2. File size exceeds limit
3. Corrupted video file
4. Network issues during upload

**Solutions:**

1. **Verify video format:**
   ```bash
   file video.mp4
   # Should show: MP4 format
   ```

2. **Check file size:**
   ```bash
   ls -lh video.mp4
   # Ensure under 500MB
   ```

3. **Validate video integrity:**
   ```bash
   # Using ffprobe (part of FFmpeg)
   ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of csv=p=0 video.mp4
   ```

4. **Convert to supported format:**
   ```bash
   ffmpeg -i input.avi -c:v copy output.mp4
   ```

5. **Compress large videos:**
   ```bash
   ffmpeg -i input.mp4 -crf 23 -preset fast output.mp4
   ```

---

## API Response Errors

### Timeout Errors

**Symptom:** Analysis takes too long or times out

**Solutions:**

1. **Use smaller videos**
2. **Reduce video length** by trimming:
   ```bash
   ffmpeg -i input.mp4 -ss 00:00:00 -t 00:05:00 -c copy output.mp4
   ```
3. **Use key_nodes analysis** for faster results
4. **Check network connection**

---

### Rate Limit Errors

**Symptom:** Too many requests in short time

**Solutions:**

1. **Add delay between requests:**
   ```python
   import time
   for video in videos:
       result = analyzer.analyze_video(video, "general")
       time.sleep(1)  # Wait 1 second between requests
   ```

2. **Use batch processing sparingly**
3. **Contact API provider** for rate limit increase

---

## Common Issues Quick Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `FileNotFoundError` | Wrong path | Verify file exists |
| `ValueError` | Invalid parameter | Check analysis type |
| `RuntimeError` | Missing dependency | `pip install openai` |
| `401 Unauthorized` | Bad API key | Verify ARK_API_KEY |
| `ModuleNotFoundError` | Missing package | Install requirements |
| `Upload failed` | Wrong format | Use MP4, check size |
| `Timeout` | Large video | Use smaller video |

---

## Debugging Tips

### Enable Verbose Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check Video Info

```python
import os
video_path = "video.mp4"
print(f"File exists: {os.path.exists(video_path)}")
print(f"File size: {os.path.getsize(video_path)} bytes")
print(f"File readable: {os.access(video_path, os.R_OK)}")
```

### Test API Connection

```python
import requests

api_key = os.environ.get("ARK_API_KEY")
if api_key:
    print(f"API key set: {api_key[:10]}...")
else:
    print("API key not set!")
```

---

## Getting Help

If you encounter errors not covered here:

1. Check the API service status
2. Review service-specific documentation
3. Search for similar issues in documentation
4. Contact support with error message and reproduction steps
