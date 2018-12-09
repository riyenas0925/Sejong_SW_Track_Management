from django.db import models
from django.utils import timezone

# Create your models here.

##########전체 트랙 정보###########
class Track(models.Model):
    name=models.CharField(max_length=15)
    tag=models.CharField(max_length=1)

    def __str__(self):
        return self.name

class SubList(models.Model):
    name=models.CharField(max_length=15)
    tagA=models.CharField(max_length=15)
    tagB=models.CharField(max_length=15)

    def __str__(self):
        return self.name


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