from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog_look/(?P<pk>\d+)/$', views.blog_look, name='blog_look'),
]