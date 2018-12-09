from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Track
from .models import SubList

import datetime
# Create your views here.

def post_list(request):
	tracks = Track.objects.all()
	sublists = SubList.objects.all()

	posts = Post.objects.filter(published_date__lte=timezone.now())

	context= { 'posts' : posts , 'tracks':tracks, 'sublists':sublists }
	return render(request, 'home/home.html',context)
