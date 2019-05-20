from django.db import models
from myutils.base_model import BaseModel
from mdeditor.fields import MDTextField
from django.utils.safestring import mark_safe
# Create your models here.

class Banner(BaseModel):
    """首页轮播图模型类"""
    image = models.ImageField(upload_to='banner', verbose_name='首页轮播图')


    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = verbose_name

class ArticleType(models.Model):
    """首页导航栏种类模型类"""
    type = models.CharField(max_length=20, verbose_name='导航栏名称')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = '首页导航种类'
        verbose_name_plural = verbose_name

class Articles(BaseModel):
    """文章模型类"""
    image = models.ImageField(upload_to='article_images', verbose_name='文章缩略图')
    title = models.CharField(max_length=128, verbose_name='文章标题')
    summary = models.CharField(max_length=128, verbose_name='文章摘要')
    content = MDTextField(verbose_name='文章详情')
    article_type = models.ForeignKey('ArticleType', on_delete=models.CASCADE, verbose_name='文章分类')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    # 用于后台显示图片
    def image_show(self):
        try:
            img = mark_safe('<img src="{}" width="50px" />'.format(self.image.url))
        except Exception as e:
            img = ''
        return img

    image_show.short_description = '缩略图'
    image_show.allow_tags = True

