from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Track
from .models import SubList

import datetime
# Create your views here.

def post_list(request):
	tag_filterA=[]
	tag_filterB=[]

	tracks = Track.objects.all()
	sublists = SubList.objects.all()
	posts = Post.objects.filter(published_date__lte=timezone.now())
	
	for i in range(0,10):
		tag_filterA[i]=sublists[i].tagA.filter(title__icontains=tracks[i].tag)
		tag_filterB[i]=sublists[i].tagB.filter(title__icontains=tracks[i].tag)

	context= { 'posts' : posts , 
			   'tracks':tracks, 
			   'sublists':sublists,
			   'tag_filterA':tag_filterA,
			   'tag_filterB':tag_filterB,
	}
	return render(request, 'home/home.html',context)

def tag_filter():
	return 0