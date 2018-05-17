from django.conf.urls import url
from app1 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 日期归档跳转
    url(r'^([0-9]{4}|[a-z]+)/$', views.catalog_p, name='year_month_article'),  # todo 未做标签页
    # 分类跳转
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.year_month_article, name='year_month_article'),
    # # 标签跳转
    # url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.year_month_article, name='year_month_article'),
    # 文章显示
    url(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})$', views.article, name='article'),
]