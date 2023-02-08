from .common import Common


class Dev(Common):
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True

    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ("drf_spectacular",)

    # schema settings, for debug
    SPECTACULAR_SETTINGS = {
        "TITLE": "Simple Order API",
        "DESCRIPTION": "The backend api for simple-order",
        "VERSION": "1.0.0",
        "SCHEMA_PATH_PREFIX": "/api",
    }

    REST_FRAMEWORK = Common.REST_FRAMEWORK
    REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"
