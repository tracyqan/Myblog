
from .models import UserIp, RequestDetail, AllRequestCount, DayRequestCount
from blog.models import Articles
from django.utils import timezone
import requests

def query_ip_place(ip):
    url = 'http://ip.taobao.com/service/getIpInfo2.php'
    params = {'ip': ip}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    try:
        res = requests.get(url, headers=headers, params=params)
        ip_data = res.json()
    except:
        ip_data = None
    return ip_data


def request_count(func):
    def count(self, request, *args, **kwargs):
        date = timezone.now().date()
        if request.META.get('HTTP_X_FORWARD_FOR'): # HTTP_X_FORWARD_FOR获取的是真实ip
            ip = request.META['HTTP_X_FORWARD_FOR']
        else:
            ip = request.META['REMOTE_ADDR']           # REMOTE_ADDR获取的是代理ip
        # 查询ip归属地
        ip_place = ''
        ip_data = query_ip_place(ip)
        if ip_data:
            country = ip_data['data']['country']
            region = ip_data['data']['region']
            city = ip_data['data']['city']
            county = ip_data['data']['county'] if ip_data['data']['county'] != 'XX' else ''
            isp = ip_data['data']['isp']
            ip_place = '-'.join([country, region, city, county, isp])

        # 尝试查询用户ip是否已存在
        try:
            user = UserIp.objects.get(ip=ip)
            user.count += 1
        except UserIp.DoesNotExist: # 不存在说明是新用户,创建新数据
            user = UserIp(ip=ip, ip_place=ip_place)
        user.save()
        # 获取目前网站总请求次数
        try:
            all_request_count = AllRequestCount.objects.get(id=1)
            all_request_count.count += 1
        except AllRequestCount.DoesNotExist:
            all_request_count = AllRequestCount()
        all_request_count.save()

        # 获取当日网站请求次数
        try:
            day_request_count = DayRequestCount.objects.get(day=date)
            day_request_count.count += 1
        except DayRequestCount.DoesNotExist:
            day_request_count = DayRequestCount(day=date)
        day_request_count.save()

        # 当前请求时间记为用户此次访问时间
        user_date = timezone.now()
        article_id = kwargs.get('id')
        if article_id:
            try:
                url = Articles.objects.get(id=article_id).title
            except Articles.DoesNotExist:
                url = Articles.objects.get(id=1).title
        else:
            url = '首页'
        request_date = RequestDetail(date=user_date, user_ip=user, url=url, ip_place=ip_place)
        request_date.save()
        return func(self, request, *args, **kwargs)
    return count



