from django.urls import path

from app import views

urlpatterns = [
    path('demo/',views.Demo.as_view()),
    path('user/',views.UserAPIView.as_view())
]