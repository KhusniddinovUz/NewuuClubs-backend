from django.urls import path
from .views import LoginAPI, RegisterAPI, UserUpdateAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path("update/", UserUpdateAPI.as_view())
]
