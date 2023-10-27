# pages/urls.py
from django.urls import path, re_path
from .views import AboutPageView, HomePageView


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("home/", HomePageView.as_view(), name="home"),
    re_path(r"^doma/$", HomePageView.as_view(), name="doma"),
    re_path(r"^$", HomePageView.as_view(), name="root"),
]
