from django.conf.urls import patterns, include, url
from blog.views import AddPost , ListPost, DetailPost, AddComment, DetailPost2
from blog import views

urlpatterns = patterns('',
	
    url(r'^login/$', views.user_login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^addpost/$', AddPost.as_view(), name = 'addpost'),
    url(r'^addcomment/$', AddComment.as_view(), name = 'addcomment'),
    url(r'^(?P<pk>[\d]+)/fullpost/$', DetailPost.as_view(), name='detailpost' ),
    url(r'^(?P<pk>[\d]+)/mainblog2/$', DetailPost2.as_view(), name='detailpost' ),
)
