
# from fastapi import FastAPI, APIRouter, Depends,UploadFile
# import os
# from src.helpers.config import get_settings, Settings
# from controllers import DataController
from os import stat

from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from src.helpers.config import get_settings, Settings
from src.controllers.DataController import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)


@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):

    is_valid, result_signal = DataController().validate_uploaded_file(file=file)

    # ✅ أولاً تحقق إذا الملف غير صالح
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}
        )

    # ✅ إذا الملف صالح، رجّع 200
    return {
        "signal": result_signal
    }
