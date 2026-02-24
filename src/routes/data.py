from fastapi import APIRouter, Depends, UploadFile, File
from controllers.DataController import DataController
import os
from helpers.config import get_settings, Settings

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)


@data_router.post("/upload/{project_id}")
async def upload_file(
    project_id: str,
    file: UploadFile = File(...),
    app_settings: Settings = Depends(get_settings)
):
    is_valid = DataController().validate_uploaded_file(file, app_settings)
    if not is_valid:
        return {"error": "Invalid file type or size"}

    upload_dir = os.path.join("uploads", project_id)
    os.makedirs(upload_dir, exist_ok=True)
    file_location = os.path.join(upload_dir, file.filename)

    # ✅ استخدم await لأن UploadFile async
    contents = await file.read()
    with open(file_location, "wb") as f:
        f.write(contents)

    return {
        "message": f"File '{file.filename}' uploaded successfully to project '{project_id}'."
    }