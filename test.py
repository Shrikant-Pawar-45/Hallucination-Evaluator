"""Sanitized example test for listing available Gemini models.

This script demonstrates how to configure the library using an environment
variable (do NOT hard-code API keys in source files).
"""
import os
import google.generativeai as genai

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    print("Set GEMINI_API_KEY in your environment to run this example.")
else:
    genai.configure(api_key=API_KEY)
    for m in genai.list_models():
        print(m.name)
