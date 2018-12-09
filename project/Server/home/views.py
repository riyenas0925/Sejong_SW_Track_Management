
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import TrackList
from .models import BsubList
from .models import AsubList

import datetime
# Create your views here.

def post_list(request):
	tracklists = TrackList.objects.all()
	bsublists=BsubList.objects.all()
	asublists=AsubList.objects.all()

	posts = Post.objects.filter(published_date__lte=timezone.now())

	context= { 'posts' : posts , 'tracklists':tracklists, 'bsublists':bsublists,'asublists':asublists}

	return render(request, 'home/home.html',context)