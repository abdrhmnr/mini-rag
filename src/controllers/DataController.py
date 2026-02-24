from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size.scale = 1024 * 1024  # Scale size to MB
    def validate_file(self, file: UploadFile, app_settings):
        # Implement file validation logic here
        if file.content_type not in app_settings.FILE_ALLOWED_TYPES:
            raise ValueError("File type not allowed")
        if file.size > app_settings.FILE_MAX_SIZE:
            raise ValueError("File size exceeds maximum allowed size")
        