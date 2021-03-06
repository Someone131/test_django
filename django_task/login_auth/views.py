from django.shortcuts import render
from django.shortcuts import render, get_object_or_404  # render page, return data or 404 page
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.contrib import auth
from polls.models import Post

# Create your views here.
def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username',"")
        password = request.POST.get('password',"")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            posts = Post.objects.filter(author=user).order_by('-published_date')
            context = {'posts': posts}
            return render(request, 'blog.html', context)
        else:
            login_error = "User not exist"
            context = {"login_error": login_error}
            return render(request, 'login_err.html', context)
    else:
        return render(request, 'login_err.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/") # модуль производит logout пользователя и перезапускает страницу