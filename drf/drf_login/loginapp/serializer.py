from rest_framework import serializers

from loginapp.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields应该写哪些字段  应该填写序列化与反序列化所需字段的并集
        fields = ("username", "password", "email")


    def validate(self, attrs):
        print(attrs)
        return attrs

    def validate_username(self, obj):
        print(obj)
        return obj


