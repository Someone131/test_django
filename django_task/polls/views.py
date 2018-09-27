from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import auth
from polls.forms import PostForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    username = auth.get_user(request).username
    context = {'posts': posts, 'username' :username}
    return render(request, 'index.html', context)

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
    posts = Post.objects.filter(author=user).order_by('-published_date')
    context = {'posts': posts, 'user': user}
    return render(request, 'blog.html', context)

def blog_look(request, pk):
    user = auth.get_user(request)
    post = get_object_or_404(Post, pk=pk)
    author = post.author
    posts = Post.objects.filter(author=author).order_by('-published_date')
    context = {'posts': posts, 'user':author}
    if user == author:
        return render(request, 'blog.html', context)
    else:
        return render(request, 'blog_look.html', context)