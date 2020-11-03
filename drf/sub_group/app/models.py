from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 这个表继承这个类, 然后这个表就拥有这些字段了

    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = "app_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

