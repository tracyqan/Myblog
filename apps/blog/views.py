
import json
from datetime import datetime
import markdown
from django.core.cache import cache
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from usercount.request_count import request_count
from .models import Banner, ArticleType, Articles


# Create your views here.


# 127.0.0.1:8000/?type= & page=

class IndexView(View):
    """首页视图"""

    @request_count
    def get(self, request):
        # 尝试从缓存中获取数据
        context = cache.get('index_cacha_data')

        if not context:
            # 获取首页轮播图
            banners = Banner.objects.all()
            # 获取首页导航条类别
            types = ArticleType.objects.all()
            # 获取最新文章
            new_articles = Articles.objects.all().order_by('-create_time')

            context = {
                'banners': banners,
                'types': types,
                'new_articles': new_articles,
            }
            # 设置缓存
            cache.set('index_cache_data', context, 3600)


        return render(request, 'index.html', context=context)

# 127.0.0.1:8000/pageAjax?page=

class AjaxView(View):
    """最新文章列表Ajax请求视图"""

    def get(self, request):
        # 获取最新文章
        try:
            type_id = int(request.GET.get('type_id', 1))
        except ValueError:
            type_id = 1
        if type_id == 1:
            new_articles =  Articles.objects.all().order_by('-create_time')
        else:
            try:
                new_articles = Articles.objects.filter(article_type=type_id).order_by('-create_time')
            except Articles.DoesNotExist:
                new_articles = Articles.objects.filter(article_type=2).order_by('-create_time')
        # 生成Paginator对象,每4个展示一页
        paginator = Paginator(new_articles, 4)
        # 获取当前页数, 默认为1
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            page = 1
        try:
            # 获取当前页码的文章
            new_articles = paginator.page(page)
        except PageNotAnInteger:
            # 当前页数不是整数返回第一页
            new_articles = paginator.page(1)
        except EmptyPage:
            # 当前页数超过最大值返回最后一页
            new_articles = paginator.page(paginator.num_pages)

        article_list = [[i.image.url, i.id, i.title, datetime.strftime(i.create_time, '%Y-%m-%d %H:%M:%S'), i.summary] for i in new_articles]

        data = {
            'result': article_list,
            'num_pages': paginator.num_pages,
            'page_id': page,
        }

        return HttpResponse(json.dumps(data))

# 127.0.0.1:8000/article/id
class ArticleDetail(View):
    """文章详情视图"""

    @request_count
    def get(self, request, id):

        try:
            article = Articles.objects.get(id=id)
        except Articles.DoesNotExist:
            article = Articles.objects.get(id=1)
        # 实现页码展示markdown文本,并且代码高亮
        article.content = markdown.markdown(article.content.replace("\r\n", '  \n'), extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ], safe_mode=True, enable_attributes=False)
        # 详情页面下方上一篇和下一篇文章的查询
        type = article.article_type
        article_list = list(Articles.objects.filter(article_type=type))
        curr_index = article_list.index(article)
        prev_article =  article_list[curr_index - 1] if curr_index>0 else None
        try:
            next_article = article_list[curr_index + 1]
        except IndexError:
            next_article = None

        context = {
            'article': article,
            'prev_article': prev_article,
            'next_article': next_article,
        }
        return render(request, 'detail.html', context=context)
