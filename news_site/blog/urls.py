import django
from django.conf.urls import include, url
from django.contrib import admin
import os
from blog import views

#app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/login/$', views.login, name='login'),
    url(r'^auth/logout/$', views.logout, name='logout'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog_look/(?P<pk>\d+)/$', views.blog_look, name='blog_look'),
    url(r'^subscribe/(?P<author>\d+)/$', views.subscribe, name='subscribe'),

]