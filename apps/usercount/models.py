from django.db import models
from django.utils import timezone


# Create your models here.
class UserIp(models.Model):
    """记录请求的用户ip和访问时间"""
    ip = models.CharField(verbose_name='IP地址', max_length=30)
    count = models.IntegerField(verbose_name='访问次数', default=1)
    ip_place = models.CharField(verbose_name='IP归属地', max_length=30, default='无')

    class Meta:
        verbose_name = '访问用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip


class RequestDetail(models.Model):
    """记录访问时间"""
    date = models.DateTimeField(verbose_name='访问时间', default=timezone.now)
    url = models.CharField(verbose_name='访问的页面', max_length=256)
    # time = models.CharField(verbose_name='滞留时长', max_length=10)  # 后续用js定时器实现
    user_ip = models.ForeignKey('UserIp', on_delete=models.CASCADE, verbose_name='IP地址')
    ip_place = models.CharField(verbose_name='IP归属地', max_length=30, default='无')

    class Meta:
        verbose_name = '访问记录详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_ip


class AllRequestCount(models.Model):
    """统计网站访问总次数"""
    count = models.IntegerField(verbose_name='网站访问总次数', default=1)

    class Meta:
        verbose_name = '网站访问总次数'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.count)
    

class DayRequestCount(models.Model):
    """统计网站单日访问次数"""
    day = models.DateField(verbose_name='日期')
    count = models.IntegerField(verbose_name='单日访问次数', default=1)

    class Meta:
        verbose_name = '网站日访问量'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.day)