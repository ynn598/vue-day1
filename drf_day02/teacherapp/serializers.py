from django.conf import settings
from rest_framework import serializers
from teacherapp.models import Teacher


#  序列化, 从后台取出数据展示在页面
class TeacherSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    # 自定义性别
    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        # gender 值是choices类型 get_字段名_display直接访问值
        print(obj.get_gender_display())
        return obj.get_gender_display()

    pic = serializers.SerializerMethodField()
    def get_pic(self, obj):
        print(obj.pic)
        return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))


# 反序列化, 将数据存入后端
class TeacherDeSerializer(serializers.Serializer):
    # 添加校验规则
    username = serializers.CharField(
        max_length=3,
        min_length=2,
        error_messages={
            "max_length": "名字太长了",
            "min_length": "名字太短了",
        }
    )
    password = serializers.CharField()
    phone = serializers.CharField()


    # 如果想要完成对象的新增 必须重写create方法
    # self是序列化器对象  validated_data需要保存的数据
    def create(self, validated_data):
        print(self)
        print(validated_data)
        return Teacher.objects.create(**validated_data)