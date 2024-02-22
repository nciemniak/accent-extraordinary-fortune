from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("zodiac_animal", views.zodiac_animal, name="zodiac_animal"),
]