from .BaseController import BaseController
from fastapi import UploadFile
from models.enums import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # Scale size to MB
        
    def validate_file(self, file: UploadFile, UploadFile, app_settings):
        # Implement file validation logic here
        if file.content_type not in app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED
        if file.size > self.size_scale * app_settings.FILE_MAX_SIZE:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED
        return True, ResponseSignal.FILE_VALIDATION_SUCCESS