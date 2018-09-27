from django.conf.urls import url
from login_auth import views as login_views
from django.conf import settings

urlpatterns = [
    url(r'^auth/login/$', login_views.login, name='login'),
    url(r'^auth/logout/$', login_views.logout, name='logout'),
    #url(r'^auth/login/blog$', login_views.login, name='login.blog'),
]