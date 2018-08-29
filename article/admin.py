#把Article,Tag,Comment添加到后台管理
from django.contrib import admin
from article.models import Article,Tag,Comment

# Register your models here.
# admin.site.register(Article)
#admin.site.register(Tag)
#admin.site.register(Comment)
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time','content')
    list_per_page = 5
    search_fields = ['title', ]
    list_filter = ['date_time', ]

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 5
    search_fields = ['name', ]
    list_filter = ['name', ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'username','content')
    list_per_page = 5
    search_fields = ['articles','username','content',]
    list_filter = ['article', ]

admin.site.register(Article, BlogAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

