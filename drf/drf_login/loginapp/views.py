from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status

from loginapp.models import User
from loginapp.serializer import UserModelSerializer


class UsesAPIView(viewsets.ViewSet):
    def login(self, request, *args, **kwargs):

        request_data = request.data  # 是个字典
        if request_data.get("username") and request_data.get("password"):

            res = User.objects.filter(username=request_data.get("username"), password=request_data.get("password"))

            if res:
                res_ser = UserModelSerializer(res[0]).data
                return Response({
                    "status": status.HTTP_200_OK,
                    "message": "登陆成功",
                    "results": res_ser
                })
            else:
                return Response({
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "登陆失败",
                })
        return Response({
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "输入不合法, 请重新输入",
        })


class RegisterAPIView(viewsets.ViewSet):

    def register(self, request, *args, **kwargs):
        request_data = request.data
        username = request_data.get("username")
        password = request_data.get("password")
        email = request_data.get("email")
        if username and password and email:
            res = User.objects.filter(username=username)
            if not res:
                res_ser = UserModelSerializer(data=request_data)
                if res_ser.is_valid():
                    user = res_ser.save()
                    return Response({
                        "status": status.HTTP_200_OK,
                        "message": "注册成功",
                        "results": UserModelSerializer(user).data
                    })
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "此用户已存在",
            })
        return Response({
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": "注册失败",
        })
