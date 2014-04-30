from django.conf.urls import patterns, include, url
from blog.views import ListPost
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ArticleBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
   
    url(r'^$', ListPost.as_view(), name = 'listpost'),
    #url(r'^$', 'blog.views.mainpage',),
    
)
