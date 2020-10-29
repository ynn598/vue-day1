from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# 当注释掉全局CSRF时, 想单独为某一个加CSRF, 使用 @csrf_protect即可

#   为视图单独去掉CSRF请求
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User


@csrf_exempt
def user(request):
    if request.method == "GET":
        print('GET查询')
        username = request.GET.get('username')
        print(username)
        return HttpResponse('get ok')

    if request.method == 'POST':
        print('post')
        return HttpResponse("postok")

    if request.method == 'DELETE':
        print('delete')
        return HttpResponse("delete ok")

    if request.method == 'PUT':
        print('put')
        return HttpResponse("put ok")

# 函数视图, 基于函数去定义视图
# 类视图   基于类定义的视图

# 定义类视图
@method_decorator(csrf_exempt,name='dispatch')  #免除csrf验证
# @method_decorator(csrf_protect,name='dispatch')  #为类视图添加csrf验证
class UserView(View):
    def get(self, request, *args, **kwargs):
        '''

                :param request:
                :param args:
                :param kwargs:
                :return:
                '''
        user_id = kwargs.get('id')
        print(user_id)
        user = User.objects.filter(pk=user_id).values("username",'password','gender').first()
        print(user)
        if user_id:
            return JsonResponse({
                'status':200,
                'message':'查询单个用户成功',
                'result':user,
            })
        else:
            all_user = User.objects.all().values('username','password','gender')
            if all_user :
                return JsonResponse({
                    'status': 200,
                    'message': '查询所有用户成功',
                    'result': list(all_user),
                })

        return JsonResponse({
            'status': 400,
            'message': '查询单个用户失败',
        })
        print('get查询')
        return HttpResponse('get ok')

    def post(self, request, *args, **kwargs):

        # 首先接收前端传来的参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.create(username=username,password= password)
            return JsonResponse({
                'status':200,
                'message':'新增成功',
                'result':{'username':user_obj.username,'gender':user_obj.gender}
            })
        except:
            return JsonResponse({
                'status': 400,
                'message': '新增失败',
            })

        print('post查询')
        return HttpResponse('post ok')

    def put(self, request, *args, **kwargs):
        print('put查询')
        return HttpResponse('put ok')

    def delete(self, request, *args, **kwargs):
        print('delete查询')
        return HttpResponse('delete ok')

class StudentAPIView(APIView):
    def get(self,request, *args,**kwargs):
        print('get')
        return Response('drf get_ok')

