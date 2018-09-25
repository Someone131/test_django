from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    #def __init__(self, title, date, text):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)
    #author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
'''    
class Blog (models.Model):
    def __init__(self):
        super.__init__()
        self.news_feed = {}  # словарь с лентой новойстей, где ключ - тема, значение - текст
        self.subscribers = {}  # словарь с подписчиками, где где ключ - имя пользователя - подписчика,
        # значение - электронная почта подписчика
        self.subscribed = {}  # словарь с пользователями, на которые подписан, где где ключ - имя пользователя,
        # значение - электронная почта пользователя
        self.posts = {} # словарь с постами пользователя


    def send_message(self, message, user):  
        pass

    def new_post(self, title, text):
        post=Post(title, text)
        self.posts.append(post)
        for user in self.subscribers.items():
            self.send_message(("User " + user.key + "aded new post: " + title + "/n" + text, user))

    def subscribe(self, user):  # метод - подписка на другого пользователя
        self.subscribed.append(user)
        pass

    def unsubscribe(self, user):  # метод - отписаться от другого пользователя
        self.subscribed.pop(user.key)
        pass
    '''