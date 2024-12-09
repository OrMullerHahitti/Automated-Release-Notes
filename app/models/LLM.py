# backend/app/models/LLM.py

from pydantic import BaseModel
from typing import List

class GenerateRequest(BaseModel):
    project_id: str
    release_id: str
    commit_messages: List[str]

class GenerateResponse(BaseModel):
    release_notes: str


# Define Pydantic model for request parameters
class WorkItemsRequest(BaseModel):
    start_date: str
    end_date: str
    organization: str
    project: str
    repository: str
