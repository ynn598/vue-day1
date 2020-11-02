from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status

def exception_handler(exc, context):

    # 打印异常信息内容
    # print(exc)
    # print(context)
    error = "%s %s %s" %(context['view'],context['request'].method, exc)
    print(error)

    response = drf_exception_handler(exc, context)

    if response is None:
        return Response({'error_message':'上帝请稍等, 程序员正在加紧处理异常'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response





