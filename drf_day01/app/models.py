from django.db import models


class User(models.Model):
    gender_choices = (
        (0, "male"),
        (1, "female"),
        (2, "其他"),
    )

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        db_table = "t_user"
        verbose_name="用户"
        verbose_name_plural = verbose_name


    def __str__(self):
        # 格式化, 使返回的不是一个对象, 而是一个用户名
        return self.username
