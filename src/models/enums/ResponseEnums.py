from enum  import Enum
 
class ResponseSignal(str, Enum):
    
    FILE_VALIDATION_SUCCESS = "file_validation_success"
    FILE_VALIDATION_FAILURE = "file_validation_failure"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILURE = "file_upload_failure"