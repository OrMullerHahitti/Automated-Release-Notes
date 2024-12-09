from fastapi import APIRouter,HTTPException,Query
from fastapi.exception_handlers import http_exception_handler

from app.services.azure_devops_services import fetch_work_items

router = APIRouter()

@router.get("/work-tems")
async def get_work_items(
    request: WorkItemFetchRequest)
    '''
    
    Fetch work items (User Stories,Features,Tasks) from azure devops based on range
    '''
    try:
        work_items =await fetch_work_items(request.start_date, request.end_date)
        return work_items
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))
    

