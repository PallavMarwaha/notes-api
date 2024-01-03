from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path("<int:id>/", views.note_view, name="detail-view"),
    path("<int:id>/share/", views.share, name="share"),
    path("search", views.search, name="search"),
    path("", views.note_view, name="views"),
]
