#!/usr/bin/env python3
"""
Response Extractor - Extracts text content from various API response formats
"""

from typing import Any, Iterable, Optional


def _iter_safe(value: Any) -> Iterable[Any]:
    """Safely iterate over a value"""
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return value
    return [value]


def extract_text_from_response(response: Any) -> Optional[str]:
    """
    Extract text content from OpenAI/Ark API response.

    Supports multiple response formats:
    - Responses API: response.output[*].content[*].text
    - ChatCompletions API: response.choices[0].message.content
    - Dictionary formats

    Args:
        response: API response object or dictionary

    Returns:
        Extracted text content, or None if not found
    """
    if response is None:
        return None

    # 1) OpenAI python SDK responses: response.output_text (some versions)
    output_text = getattr(response, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    # 2) Responses API: response.output[*].content[*].text
    output = getattr(response, "output", None)
    for output_item in _iter_safe(output):
        content = getattr(output_item, "content", None)
        for content_item in _iter_safe(content):
            text = getattr(content_item, "text", None)
            if isinstance(text, str) and text.strip():
                return text.strip()
            # Some implementations use dict
            if isinstance(content_item, dict):
                text = content_item.get("text")
                if isinstance(text, str) and text.strip():
                    return text.strip()

    # 3) ChatCompletions: response.choices[0].message.content
    choices = getattr(response, "choices", None)
    for choice in _iter_safe(choices):
        message = getattr(choice, "message", None)
        content = getattr(message, "content", None)
        if isinstance(content, str) and content.strip():
            return content.strip()

    # 4) Dictionary format (some providers return dict)
    if isinstance(response, dict):
        # 4.1 output_text
        output_text = response.get("output_text")
        if isinstance(output_text, str) and output_text.strip():
            return output_text.strip()

        # 4.2 responses output
        output = response.get("output")
        for output_item in _iter_safe(output):
            if isinstance(output_item, dict):
                for content_item in _iter_safe(output_item.get("content")):
                    if isinstance(content_item, dict):
                        text = content_item.get("text")
                        if isinstance(text, str) and text.strip():
                            return text.strip()

        # 4.3 chat completions
        choices = response.get("choices")
        for choice in _iter_safe(choices):
            if isinstance(choice, dict):
                message = choice.get("message") or {}
                content = message.get("content")
                if isinstance(content, str) and content.strip():
                    return content.strip()

    return None