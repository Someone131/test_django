from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import auth

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    article_status = models.IntegerField(default=0)

    def __str__(self):
        return (self.title)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    subscribed=[]

    def subscribe_on(self, author):
        self.subscribed.append(author)
        self.save()

    def subscribe_off(self, author):
        self.subscribed.remove(author)
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

