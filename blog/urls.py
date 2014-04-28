from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',

    url(r'^login/$', views.user_login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid_login, name='invalid_login'),


)
