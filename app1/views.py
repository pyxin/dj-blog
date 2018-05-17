from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Article, Tag, Catalog
import logging

logger = logging.getLogger(__name__)
from django.utils import timezone


def index(req):  # todo 未做分页
    """首页"""
    title = "首页"
    menu_list = Menu.objects.all().order_by('created_time')  # 顶部菜单数据
    # offside = Article.objects.dates('created_time', 'year', order='DESC')  # 日期按年归类
    # offside_dict = dict()
    # for i in offside:
    #     offside_dict[i.year] = Article.objects.filter(created_time__year=i.year).count()  # 当年文章总数
    offside_dates = Article.objects.dates('created_time', 'month', order='DESC')
    catalog_lsit = Catalog.objects.all()
    tag_lsit = Tag.objects.all()
    # 首页数据
    article_list = Article.objects.all().order_by('-read')  # 首页数据显示 以阅读量
    new_lsit = article_list.order_by('-created_time')[:3]  # 右侧最新文章数据

    return render(req, 'app1/index.html', locals())


def catalog_p(req, year):  # todo 未做分页
    """列表页"""
    title = "文章"
    menu_list = Menu.objects.all().order_by('created_time')  # 顶部菜单数据
    if year.isdecimal():  # 只包含数字
        offside_dates = Article.objects.dates('created_time', 'month', order='DESC')
        # offside = Article.objects.dates('created_time', 'year', order='DESC')  # 日期按年归类
        # offside_dict = dict()
        # for i in offside:
        #     offside_dict[i.year] = Article.objects.filter(created_time__year=i.year).count()  # 当年文章总数
        catalog_lsit = Catalog.objects.all()  # 右侧分类目录数据
        article_list = Article.objects.filter(created_time__year=year).order_by('created_time')
    else:
        offside_dates = Article.objects.dates('created_time', 'month', order='DESC')
        catalog_lsit = Catalog.objects.all()  # 右侧分类目录数据
        article_list = Article.objects.filter(catalog__name=year).order_by('created_time')
    tag_lsit = Tag.objects.all()  # 右侧标签数据
    # 当前菜单页数据
    new_lsit = article_list.order_by('-created_time')[:3]  # 右侧最新文章
    year_month = year
    return render(req, 'app1/index.html', locals())


def article(req, year, month, day):
    title = "文章"
    menu_list = Menu.objects.all().order_by('created_time')  # 顶部菜单数据
    offside_dates = Article.objects.dates('created_time', 'month', order='DESC')  # 右侧日期分类数据
    catalog_lsit = Catalog.objects.all()  # 右侧分类目录数据
    # article_list = Article.objects.filter(created_time__year=year).order_by('created_time')
    tag_lsit = Tag.objects.all()  # 右侧标签数据
    # new_lsit = article_list.order_by('created_time')[:3]  # 右侧最新文章数据
    ids = req.GET.get('ids')
    article_obj = Article.objects.get(pk=ids)
    new_lsit = Article.objects.filter(catalog=article_obj.catalog).order_by('-created_time')[:3]

    return render(req, 'app1/single.html', locals())
