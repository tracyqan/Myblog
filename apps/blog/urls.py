
from django.urls import re_path
from .views import IndexView, ArticleDetail, AjaxView

app_name = 'article'
urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'), # 首页
    re_path(r'^article/(?P<id>\d+)$', ArticleDetail.as_view(), name='detail'), # 文章详情页
    re_path(r'^pageAjax$', AjaxView.as_view()), # 首页文章列表
]
