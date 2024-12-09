from pydantic import BaseModel

class WorkItemFetchRequest(BaseModel):
    start_date: str
    end_date: str

