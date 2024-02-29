from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("zodiac", views.zodiac, name="zodiac"),
    path("upload_selfie", views.upload_selfie, name="upload_selfie"),
    path("result", views.result, name="result"),
    path("midjourney_task_progress", views.midjourney_task_progress, name="midjourney_task_progress"),
]