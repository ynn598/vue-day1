from django.db import models

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    email = models.CharField(max_length=80)

    class Meta:
        db_table = "t_user"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


