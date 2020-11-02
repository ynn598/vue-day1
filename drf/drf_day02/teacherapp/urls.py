from django.urls import path

from teacherapp import views

urlpatterns = [
    path('tea/',views.TeacherAPIView.as_view()),
    path('tea/<str:id>/',views.TeacherAPIView.as_view()),
]
