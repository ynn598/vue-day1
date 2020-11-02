from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import BookModelSerializer

from api.models import Book


class BookAPIView(APIView):

    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        print(book_id)
        if book_id:
            book_data = Book.objects.get(pk=book_id)
            print(book_data, 111111111111111111)
            res = BookModelSerializer(book_data).data
            print(res)
            return Response({
                "status": status.HTTP_200_OK,
                "message": "查询单本书成功",
                "results": res,
            })
        else:
            book_data = Book.objects.all()
            books_ser = BookModelSerializer(book_data, many=True).data

            return Response({
                "status": status.HTTP_200_OK,
                "message": "查询所有用户成功",
                "results":books_ser
            })
















class BookAPIView2(APIView):

    def get(self, request, *args, **kwargs):
        # 首先得到这本书的id
        book_id = kwargs.get("id")
        # 如果是一本书的id, 或者是能获取到id, 说明是一本书, 就查询的是单本书
        if book_id:
            book = Book.objects.get(pk=book_id, is_delete=False)
            data = BookModelSerializer(book).data
            return Response({
                "status": 200,
                "message": "查询单本图书成功",
                "results": data
            })
        else:
            books_result = Book.objects.filter(is_delete=False)  # 查询所有书
            print(BookModelSerializer(books_result, many=True))
            return Response({
                "status": 200,
                "message": "查询所有图书成功",
                "result": BookModelSerializer(books_result, many=True).data
            })

    # 用于增加数据
    def post(self, request, *args, **kwargs):
        request_data = request.data
        # 如果获取到的为一个字典
        if isinstance(request_data, dict):
            is_many = False
        # 如果是一个列表
        elif isinstance(request_data, list):
            is_many = True
        else:
            return Response({
                "status": 400,
                "message": "发生错误"
            })

        serializer = BookModelSerializer(data=request_data, many=is_many)
        '''
        is_valid() 方法还可以在验证失败时抛出异常 serializers.ValidationError，
        可以通过传递raise_exception=True参数开启，
        REST framework接收到此异常，会向前端返回 HTTP 400 Bad Request响应。
        '''
        serializer.is_valid(raise_exception=True)  # 抛出异常
        book_obj = serializer.save()
        return Response({
            "status": 200,
            "message": "添加成功",
            "results": BookModelSerializer(book_obj, many=is_many).data,
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get("id")

        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get("ids")

        response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)

        if response:
            return Response({
                'status': 200,
                "message": "删除成功",
            })
        return Response({
            "status": 400,
            'message': "该图书不存在或删除失败"
        })

    # 修改
    def put(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get('id')

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": "图书不存在"
            })

        serializer = BookModelSerializer(data=request_data, instance=book_obj)
        serializer.is_valid(raise_exception=True)

        # 经过序列化器对   全局钩子与局部钩子校验后  开始更新
        serializer.save()

        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })

    def patch(self, request, *args, **kwargs):
        """
        整体修改单个:  修改一个对象的全部字段
        修改对象时,在调用序列化器验证数据时必须指定instance关键字
        在调用serializer.save() 底层是通过ModelSerializer内部的update()方法来完成的更新
        """

        # 获取要修改的对象的值
        request_data = request.data
        # 获取要修改的图书的id
        book_id = kwargs.get("id")

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })

        # 更新的时候需要对前端传递的数据进行安全校验
        # 更新的时候需要指定关键字参数data
        # TODO 如果是修改  需要自定关键字参数instance  指定你要修改的实例对象是哪一个
        serializer = BookModelSerializer(data=request_data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)

        # 经过序列化器对   全局钩子与局部钩子校验后  开始更新
        serializer.save()

        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })

    # 群体修改, new data



