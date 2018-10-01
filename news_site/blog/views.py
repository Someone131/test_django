from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Post, Profile
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import PostForm
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    username = auth.get_user(request).username
    context = {'posts': posts, 'username': username}
    return render(request, 'index.html', context)

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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def blog(request):
    user = auth.get_user(request)
    list=[]
    posts = Post.objects.filter(author=user).order_by('-published_date')
    if Profile.subscribed ==[]:
        for i in posts:
            list.append(i)
    else:
        for i in Profile.subscribed:
            post = Post.objects.filter(author=i)
            list.append(post)
    context = {'posts': list, 'user': user}
    return render(request, 'blog.html', context)

def blog_look(request, pk):
    user = auth.get_user(request).username
    post = get_object_or_404(Post, pk=pk)
    author = post.author
    posts = Post.objects.filter(author=author).order_by('-published_date')
    if author in Profile.subscribed:
        status = f"Вы подписаны на пользователя {author}. Отменить подписку?"
    else:
        status = f"Подписаться на пользователя {author}?"
    if user == author:
        return render(request, 'blog.html', {'posts': posts, 'user':author})
    else:
        return render(request, 'blog_look.html', {'posts': posts, 'user':author,'status':status, 'value':Profile.subscribed})

def subscribe(request, author):
    user = auth.get_user(request).username
    author = get_object_or_404(User, pk=author)
    #author = author
    if author in Profile.subscribed:
        Profile.subscribed.remove(author)
        massage = "Подписка на пользователя отменена"
    else:
        Profile.subscribed.append(author)
        massage = "Вы подписаны на пользователя"
    return redirect('/')
