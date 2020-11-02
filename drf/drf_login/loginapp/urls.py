from django.urls import path

from loginapp import views

urlpatterns = [
    path('login/', views.UsesAPIView.as_view({"post": "login",})),
    path('login/<str:id>/', views.UsesAPIView.as_view({"post": "login",})),
    path("register/", views.RegisterAPIView.as_view({"post":"register"})),
    path("register/<str:id>/", views.RegisterAPIView.as_view({"post":"register"})),
]
