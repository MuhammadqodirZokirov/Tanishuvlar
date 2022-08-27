import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default='998991112233', blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=100, blank=True)
    profile_img = models.ImageField(upload_to='profiles/', blank=True)
    bg_img = models.ImageField(upload_to='bg_img/', blank=True)
    reyting = models.IntegerField(default=0, blank=True)
    pul = models.IntegerField(default=0, blank=True)
    city = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50, default='Male', blank=True)
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_online = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Foydalanuchilar'

    def last_seen(self):
        return cache.get('last_seen_%s' % self.user.username)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > (self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)):
                return False
            else:
                return True
        else:
            return False


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=True)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)



class PhotoDuel(models.Model):
        foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='foydalanuvchi')
        photos = models.ImageField(upload_to='duel/', blank=True, null=True)
        like = models.IntegerField(default=0, blank=True, null=True,)

        def __str__(self):
            return self.foydalanuvchi

