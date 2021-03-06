from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home'),
    url(r'^$', 'article.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^tag/(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    #url(r'^search/$','article.views.blog_search', name = 'search'),
    #url(r'^add_comment/(?P<pk>\d+)/$','article.views.add_comment',name='add_comment'),
]
