"""news_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views

'''
admin.autodiscover()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_site.settings")
django.setup()
'''

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^', include('login_auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^auth/login/$', views.login, name='login'),
    url(r'^auth/logout/$', views.logout, name='logout'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^blog/$', views.blog, name='blog'),
    #url(r'^blog_look/(?P<pk>\d+)/$', views.blog_look, name='blog_look'),
    #url(r'^subscribe/(?P<author>\d+)/$', views.subscribe, name='subscribe'),
]
