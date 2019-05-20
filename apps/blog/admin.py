from django.contrib import admin
from .models import Banner, ArticleType, Articles

# Register your models here.

# 修改后台网页显示的标题
admin.site.site_title = 'Python'
admin.site.site_header = 'LovePython'
admin.site.index_title = 'Love'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'image',
        'create_time',
        'update_time',
        'is_delete',
    ]
    # list_editable 设置默认可编辑字段（第一个字段默认不可编辑，因为它是一个链接,点击会进入修改页面)
    #  如果需要编辑要将一个不需要编辑的字段设置到list_display_links）
    list_editable = ['image']
    # list_display_links = ['id']

@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'type',
    ]
    list_editable = ['type']
    list_display_links = ['id']

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'article_type',
        'summary',
        # 'content',
        'image_show',
        'create_time',
        'update_time',
        'is_delete',
    ]
    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('create_time',)

    list_editable = ['summary', 'article_type',]

    # 过滤器功能及能过滤的字段
    list_filter = ('title', 'article_type')
    # 搜索功能及能实现搜索的字段
    search_fields = ('title', 'article_type',)
    # 详细时间分层筛选
    date_hierarchy = 'create_time'