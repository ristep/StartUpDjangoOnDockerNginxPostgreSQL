from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("static_pages.urls")),
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),
    path("api/", include("jwt_token.urls")),
    path("upload/", include("upload.urls")),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
