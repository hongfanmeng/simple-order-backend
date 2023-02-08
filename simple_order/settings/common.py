from dotenv import load_dotenv
from pathlib import Path
import os
import dj_database_url
from configurations import Configuration

# Take environment variables from .env.
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Common(Configuration):
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "django-insecure-6(n&s3l@f#_%&r7y$lc13(ieg0jjeopno^m5mdarf4khawacm&",
    )

    # Application definition
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # drf
        "rest_framework",
        "rest_framework.authtoken",
        "rest_framework_json_api",
        # auth
        "dj_rest_auth",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "dj_rest_auth.registration",
        # modules
        "users",
        "ordering",
    ]
    REST_FRAMEWORK = {
        # json:api settings
        "PAGE_SIZE": 10,
        "EXCEPTION_HANDLER": "rest_framework_json_api.exceptions.exception_handler",
        "DEFAULT_PAGINATION_CLASS": "rest_framework_json_api.pagination.JsonApiPageNumberPagination",
        "DEFAULT_PARSER_CLASSES": (
            "rest_framework_json_api.parsers.JSONParser",
            "rest_framework.parsers.FormParser",
            "rest_framework.parsers.MultiPartParser",
        ),
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework_json_api.renderers.JSONRenderer",
            # If you're performance testing, you will want to use the browseable API
            # without forms, as the forms can generate their own queries.
            # If performance testing, enable:
            # 'example.utils.BrowsableAPIRendererWithoutForms',
            # Otherwise, to play around with the browseable API, enable:
            "rest_framework_json_api.renderers.BrowsableAPIRenderer",
        ),
        "DEFAULT_METADATA_CLASS": "rest_framework_json_api.metadata.JSONAPIMetadata",
        "DEFAULT_SCHEMA_CLASS": "rest_framework_json_api.schemas.openapi.AutoSchema",
        "DEFAULT_FILTER_BACKENDS": (
            "rest_framework_json_api.filters.QueryParameterValidationFilter",
            "rest_framework_json_api.filters.OrderingFilter",
            "rest_framework_json_api.django_filters.DjangoFilterBackend",
            "rest_framework.filters.SearchFilter",
        ),
        "SEARCH_PARAM": "filter[search]",
        "TEST_REQUEST_RENDERER_CLASSES": (
            "rest_framework_json_api.renderers.JSONRenderer",
        ),
        "TEST_REQUEST_DEFAULT_FORMAT": "vnd.api+json",
        # auth using token
        "DEFAULT_AUTHENTICATION_CLASSES": [
            "rest_framework.authentication.TokenAuthentication",
        ],
    }

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "simple_order.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "simple_order.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv(
                "POSTGRES_CONN_URL", "postgres://postgres:postgres@db:5432/postgres"
            ),
            conn_max_age=int(os.getenv("POSTGRES_CONN_MAX_AGE", 600)),
        )
    }

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.1/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"

    USE_I18N = False

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

    # Media files
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[%(server_time)s] %(message)s",
            },
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            },
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        "filters": {
            "require_debug_true": {
                "()": "django.utils.log.RequireDebugTrue",
            },
        },
        "handlers": {
            "django.server": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "django.server",
            },
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "simple",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "propagate": True,
            },
            "django.server": {
                "handlers": ["django.server"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["mail_admins", "console"],
                "level": "ERROR",
                "propagate": False,
            },
            "django.db.backends": {"handlers": ["console"], "level": "INFO"},
        },
    }

    AUTH_USER_MODEL = "users.User"
