from django.urls import path
from .views import image_upload

urlpatterns = [
    path("", image_upload, name="upload"),
]
