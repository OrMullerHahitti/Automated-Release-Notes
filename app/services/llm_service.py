# backend/app/services/llm_service.py

import httpx

from app.models.models import Document
from app.utils.config import LLM_API_URL, LLM_API_KEY
import logging

logger = logging.getLogger(__name__)

async def generate_response(commit_messages: list) -> str:
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": "\n".join(commit_messages),
        "max_tokens": 150,
        "temperature": 0.7,
        "n": 1,
        "stop": None
    }
    async with httpx.AsyncClient() as client:
        logger.info(f"Sending request to LLM API at {LLM_API_URL}")
        response = await client.post(LLM_API_URL, json=payload, headers=headers)
        if response.status_code != 200:
            logger.error(f"LLM API error: {response.status_code} - {response.text}")
            response.raise_for_status()
        data = response.json()
        release_notes = data.get("choices", [{}])[0].get("text", "").strip()
        if not release_notes:
            release_notes = "No release notes generated."
        logger.info("Release notes generated successfully.")
        return release_notes
