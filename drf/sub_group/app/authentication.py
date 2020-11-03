from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from app.models import User

'''
1. 继承baseauthentication类,
2. 重写authenticate方法
3. 自定义认证规则:
    没有认证信息为游客; 
    有认证信息, 但是不符合要求就是非法用户
    有认证信息且合法--合法用户
'''
class MyAuth(BaseAuthentication):

    def authenticate(self,request):
        # 前端发送认证请求时, 必须携带认证信息, 还需要按照一定的格式来
        # 默认以authorization来携带用户信息
        # 认证信息都包含在request.META中
        auth = request.META.get("HTTP_AUTHORIZATION",None)
        print(auth)

        if auth is None:
            return None

        auth_split = auth.split()
        if not(len(auth_split) == 2 and auth_split[0].lower() == 'ynn'):
            raise exceptions.AuthenticationFailed("认证信息有误")

        if auth_split[1] != 'abc.subgroup.123':
            raise exceptions.AuthenticationFailed('用户信息认证失败')

        user = User.objects.filter(username='subgroup').first()
        if not user:
            raise exceptions.AuthenticationFailed("用户不存在或已删除")

        return (user,None)


