from rest_framework import serializers
from api.models import Book, Press


# class PressModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Press
#         fields = ("press_name", "address")


class BookModelSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('book_name', 'price', 'pic')

        # 添加DRF提供的默认校验规则
        extra_kwargs = {
            "book_name":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"必须提供图书名",
                    "min_length":"图书名不能少于两个字符",
                }
            },
            "pic": {
                "read_only": True
            },
            # "publish":{
            #     "write_only":True,
            # },
            # "authors":{
            #     "write_only":True,
            # },
        }

        def validate(self, attrs):
            # print(attrs)
            return attrs

        def validate_book_name(self, obj):
            # print(obj)
            return obj


class BookModelSerializer(serializers.ModelSerializer):

    class Meta:
        # 指定当前序列化器类要序列化的模型
        model = Book
        # 指定要序列化的字段
        fields = ("book_name","price","pic","aaa")

        # 序列化所有字段
        # fields = '__all__'

        # 不包含哪些字段
        # exclude = ("publish")

        # 查询的深度为 1
        # depth = '1'

