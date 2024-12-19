import datetime
from pydantic import BaseModel
import datetime as dt
class DateRange(BaseModel):
    start_date: str
    end_date: str
class WorkItemFetchRequest(BaseModel):
    start_date: str
    end_date: str
class Commit(BaseModel):
    id: str
    datetime: datetime.datetime
    message: str
    status: str
class WorkItem(BaseModel):
    id: str
    title: str
    type: str
    status: str
    assigned_to: str
class Document(BaseModel):
    title: str
    content: str



