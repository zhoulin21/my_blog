#定义模型 标签、文章和评论
# Create your models here.
from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(verbose_name='博客标签',max_length=20)
    class Meta:
        verbose_name_plural = '博客标签'  #用于django后台管理显示
    def __str__(self):
        return self.name

class Article(models.Model) :
    title = models.CharField(verbose_name='我的文章',max_length = 100)  #博客题目
    tag_name = models.ManyToManyField(Tag)  #博客与标签为多对多关系
    date_time = models.DateTimeField(verbose_name='创建时间',auto_now_add = True)  #博客日期
    content = models.TextField(verbose_name='文章内容',blank = True, null = True)  #博客文章内容
    class Meta:
        verbose_name_plural = '我的文章'
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='博客', related_name='comments') #博客与评论属于一对多关系
    username = models.CharField(verbose_name='姓名', max_length=20, default='匿名')
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.content[:10]



