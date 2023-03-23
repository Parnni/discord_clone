from base import views
from django.urls import path

urlpatterns = [
    path("home/", views.home, name="home"),
    path("room/create/", views.create_room, name="create-room"),
    path("room/<str:pk>/", views.room, name="room"),
]
