from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status


def exception_handler(exc, context):
    error = "%s %s %s" % (context["view"], context["request"].method, exc)

    response = drf_exception_handler(exc, context) # DRF处理异常
    # 如果DRF无法处理此异常 ,则自定义处理
    if response is None:
        return Response({"error_message": "上帝请稍等,程序猿正在加紧处理中~"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # 如果response不为空  说明异常已经被处理了
    return response