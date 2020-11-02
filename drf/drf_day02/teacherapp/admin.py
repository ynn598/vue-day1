from django.contrib import admin

from teacherapp import models

admin.site.register(models.Teacher)
admin.site.register(models.Student)