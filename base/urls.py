from base import views
from django.urls import path

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("home/", views.home, name="home"),
    path("room/create/", views.create_room, name="create-room"),
    path("room/update/<str:pk>", views.update_room, name="update-room"),
    path("room/delete/<str:pk>", views.delete_room, name="delete-room"),
    path("room/<str:pk>/", views.room, name="room"),
]
