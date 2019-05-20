from django.contrib import admin
from .models import UserIp, RequestDetail, AllRequestCount, DayRequestCount
# Register your models here.

@admin.register(UserIp)
class UserIpAdmin(admin.ModelAdmin):
    list_display = ('ip', 'ip_place', 'count')
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-count',)

@admin.register(RequestDetail)
class RequestDateAdmin(admin.ModelAdmin):
    list_display = ('user_ip', 'ip_place', 'date', 'url')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 20
    # 过滤器功能及能过滤的字段
    list_filter = ('user_ip', 'date', 'url', 'ip_place')
    # 搜索功能及能实现搜索的字段
    search_fields = ('user_ip', 'url', 'ip_place')
    # 详细时间分层筛选
    date_hierarchy = 'date'

@admin.register(AllRequestCount)
class AllRequestCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'count')

@admin.register(DayRequestCount)
class DayRequestCountAdmin(admin.ModelAdmin):
    list_display = ('day', 'count')

    ordering = ('day',)