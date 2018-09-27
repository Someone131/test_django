from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article_status = models.IntegerField(default=0)      # отметка о прочтении = 1

    def __str__(self):
        return (self.title)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

'''
class Blog (models.Model):
    subscribers = ()
    subscribed = ()
    
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