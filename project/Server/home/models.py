from django.db import models
from django.utils import timezone

# Create your models here.

##########전체 트랙 정보###########
class TrackList(models.Model):
    tname=models.CharField(max_length=15)
    tnum=models.IntegerField(default=0)

    def __str__(self):
        return self.tname

class BsubList(models.Model):
    tnum=models.IntegerField(default=0)
    bname=models.CharField(max_length=15)

    def __str__(self):
        return self.bname


class AsubList(models.Model):
    tnum=models.IntegerField(default=0)
    aname=models.CharField(max_length=15)

    def __str__(self):
        return self.aname

class User(models.Model):
    name=models.CharField(max_length=15)
    number=models.CharField(max_length=10)
    selectTrack=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class UserSub(models.Model):
    number=models.CharField(max_length=10)
    subject=models.CharField(max_length=15)

    def __str__(self):
        return self.subject

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

