from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User
from app.throttle import SendMessageRate


class Demo(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.first()
        print(user.groups.first())
        print(user.user_permissions.first())
        return Response("okk")

class UserAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        print("read")
        return Response('read')

    def post(self, request, *args, **kwargs):
        print('post')
        return Response('write')