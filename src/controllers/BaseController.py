from helpers.config import get_settings, Settings

class BaseController:
    def __init__(self):
        pass

    def get_app_info(self, app_settings):
        return {
            "app_name": app_settings.APP_NAME,
            "app_version": app_settings.APP_VERSION
        }