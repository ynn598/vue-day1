from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny

from app.models import User



class MyPerission(BasePermission):

    # 局部定义权限
    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]   #只允许认证成功的用户访问
    # permission_classes = [IsAdminUser]  只允许超级管理员
    # IsAuthenticatedOrReadOnly     只有认证成功的用户可以操作

    def has_permission(self, request, view):
        if request.method in ('GET','HEAD','OPTION'):
            return True
        username = request.data.get('username')
        user = User.objects.filter(username = username).first()
        print(user)

        if user:
            return True
        return False