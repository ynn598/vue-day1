from django.db import models

class Teacher(models.Model):
    gender_choices = (
        (0,"女"),
        (1,'男'),
        (2,'第三性别'),
    )

    username = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=gender_choices,default=1)
    phone = models.CharField(max_length=11,null=True,blank=True)
    pic = models.ImageField(upload_to='pic/',default='pic/917257.jpg')

    class Meta:
        db_table='t_teacher'
        verbose_name='教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

