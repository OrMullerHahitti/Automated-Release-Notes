# backend/app/routers/LLM.py
import httpx
from fastapi import APIRouter, HTTPException
from app.models.LLM import GenerateRequest, GenerateResponse
from app.services.llm_service import generate_release_notes
import logging

router = APIRouter(
    prefix="/api",
    tags=["Generate Release Notes"]
)

logger = logging.getLogger(__name__)

@router.post("/generate", response_model=GenerateResponse)
async def generate_release_notes_endpoint(request: GenerateRequest):
    try:
        logger.info(f"Generating release notes for project {request.project_id}, release {request.release_id}")
        release_notes = await generate_release_notes(request.commit_messages)
        return GenerateResponse(release_notes=release_notes)
    except httpx.HTTPStatusError as e:
        logger.error(f"LLM API returned an error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail="Error communicating with LLM API.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error.")
