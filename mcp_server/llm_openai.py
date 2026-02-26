# llm_openai.py - Local LLM Integration Example (OpenAI)
"""
This module provides a function to call OpenAI's API for agentic orchestration.
- Used by the MCP server to generate responses from a real LLM
- Logs all prompts and responses for provenance

Concept: Demonstrates how to integrate a real LLM for agentic workflows.
"""

import os
import openai
import logging

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt):
    logging.info(f"Calling OpenAI LLM with prompt: {prompt}")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256
        )
        result = response.choices[0].message["content"]
        logging.info(f"OpenAI LLM response: {result}")
        return result
    except Exception as e:
        logging.error(f"OpenAI LLM error: {e}")
        return f"Error: {e}"

# As we build, this module can be extended for other LLMs (Ollama, etc.) and richer workflows.
