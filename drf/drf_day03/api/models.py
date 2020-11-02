from django.conf import settings
from django.db import models



class BaseModel(models.Model):
    '''
    基类, 定义一些其他类中都有的列, 抽象类, 不会在数据库中进行存储
    '''
    is_delete = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to='img', default='img/1.jpg')
    address = models.CharField(max_length=256)

    class Meta:
        db_table = 'tb_press'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    # 让其他东西在调用这个类的时候, 返回的不是整个类里的东西, 可以是名字
    def __str__(self):
        return self.press_name


#  定义作者类
class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()

    class Meta:
        db_table = 't_author'
        verbose_name = "作者"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.author_name


# 定义作者的详情页
class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    # 在子表中定义外键时，增加related_name字段指定这个子表在主表中对应的外键属性
    author = models.OneToOneField(to='Author', on_delete=models.CASCADE, related_name="detail")

    class Meta:
        db_table = 't_author_detail'
        verbose_name = '作者详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s的详情' % self.author.author_name


#  书
class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.ImageField(upload_to='img', default='img/1.jpg')
    # db_constraint=False   保留跨表查询的便利, 一般设置为false
    publish = models.ForeignKey(to='Press', on_delete=models.CASCADE, db_constraint=False, related_name='books')
    authors = models.ManyToManyField(to='Author', db_constraint=False, related_name='books' )

    class Meta:
        db_table = 't_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name

    @property
    def press_name(self):
        return self.publish.press_name

    @property
    def author_list(self):
        return self.authors.values("author_name", "age", "detail__phone")

    @property
    def aaa(self):
        return "aaa"

    # @property
    # def pic(self, obj):
    #     return "%s%s%s" % ("http://127.0.0.1:8000/", settings.MEDIA_URL, str(obj.pic))