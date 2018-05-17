from django.db import models
from common.db import BaseModel
from django.contrib.auth.models import AbstractUser  # 引用django自带用户系统
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy


class User(AbstractUser, BaseModel):
    """用户"""
    nickname = models.CharField(verbose_name='昵称', max_length=30)  # 昵称
    email = models.EmailField(ugettext_lazy('email address'), unique=True)

    class Meta:
        db_table = "blog_user"  # 表名
        verbose_name = "用户"

    def generate_active_token(self):
        serializer = Serializer(settings.SECRET_KEY, 3600)
        token = serializer.dumps({'token_user_id': self.id})
        return token.decode()

    @property  # 使用 @property 装饰器装饰的方法，会把该方法提升成属性，在访问的时候，就以属性的方式去访问
    def password_hash(self):
        pass

    @password_hash.setter  # passwords被设置值的时候会调用该方法
    def password_hash(self, value):
        """创建散列密码"""
        self.password = make_password(value, settings.SECRET_KEY, 'pbkdf2_sha256')

    def check_passwords(self, password):
        """对密码进行校验"""
        return check_password(password, self.password)


# Create your models here.
class Tag(BaseModel):
    """标签"""
    tag_colour = (
        ('layui-bg-black', '黑色'),
        ('layui-bg-blue', '蓝色'),
        ('layui-bg-cyan', '青色'),
        ('layui-bg-green', '绿色'),
        ('layui-bg-orange', '橙色'),
        ('layui-bg-red', '红色'),
        ('layui-badge', '本色'),
    )
    name = models.CharField(verbose_name='标签名', max_length=64)
    style = models.CharField(verbose_name='样式颜色', max_length=30, choices=tag_colour, default='layui-badge')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "blog_tag"  # 表名
        verbose_name = "标签"


class Menu(BaseModel):
    """菜单"""
    name = models.CharField(verbose_name='菜单', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "blog_menu"  # 表名
        verbose_name = "菜单"


class Catalog(BaseModel):
    """小目录"""
    name = models.CharField(verbose_name='目录名', max_length=64)
    menu = models.ForeignKey(Menu, verbose_name='目录', on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "blog_catalog"  # 表名
        verbose_name = "目录"


class Article(BaseModel):
    """文章"""
    original_reprint = (
        ('0', '原创'),
        ('1', '转载'),
    )
    # date = models.DateField('日期统计用')
    # created_time = models.DateTimeField('创建时间', default=timezone.now)
    title = models.CharField(verbose_name='标题', max_length=200)
    digest = models.CharField(verbose_name='摘要', max_length=200, default='')
    body = models.TextField(verbose_name='正文')
    modality = models.CharField(verbose_name='文章形式', max_length=1, choices=original_reprint, default='0')  #
    # 渲染模板获取值使用get_modality_display()
    read = models.IntegerField(default=0, verbose_name="浏览量")
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True, default=1)  # 多对多关系
    catalog = models.ForeignKey(Catalog, verbose_name='分类', on_delete=models.CASCADE, default=8)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, default=1)

    # comment_num = models.IntegerField(default=0, verbose_name="评论量")

    # Forwarding_num = models.IntegerField(default=0, verbose_name="转发量")
    # collection_num = models.IntegerField(default=0, verbose_name="收藏量")
    # image_name = models.CharField('名字', max_length=20)
    # image_url = models.CharField('url', max_length=200)
    # navigation = models.ForeignKey('NavigationCatalog', verbose_name='导航', on_delete=models.CASCADE)
    def reading(self):
        self.read += 1
        self.save()  # todo 什么意思

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-read']
        db_table = "blog_article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'


class Comment(BaseModel):
    body = models.TextField(verbose_name='评论')
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ['-created_time']
        db_table = "blog_comment"
        verbose_name = "评论"
        verbose_name_plural = verbose_name
