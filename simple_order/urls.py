import os
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, re_path
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api/user/", include("users.urls")),
    re_path(r"^api/auth/", include("dj_rest_auth.urls")),
    re_path(r"^api/auth/registration/", include("dj_rest_auth.registration.urls")),
]

if os.getenv("DJANGO_CONFIGURATION", "Dev") == "Dev":
    # serve static and media when develop
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # show api doc when develop
    urlpatterns += [
        re_path(r"^api/schema/?$", SpectacularAPIView.as_view(), name="schema"),
        re_path(
            r"^api/schema/swagger-ui/?$",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        re_path(
            r"^api/schema/redoc/?$",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
