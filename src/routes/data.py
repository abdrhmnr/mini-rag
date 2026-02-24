from fastapi import APIRouter, Depends, UploadFile, File,status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)


@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile = File(...),
    app_settings: Settings = Depends(get_settings)
):
    
    
    
    
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return {"error": f"Invalid file: {signal.value}"}

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": f"File validation failed: {result_signal.value}"}
        )