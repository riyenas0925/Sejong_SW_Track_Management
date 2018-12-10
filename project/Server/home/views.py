from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django import forms
import django_excel as excel

from django.utils import timezone
from .models import Post
from .models import TrackList
from .models import BsubList
from .models import AsubList
from .models import User
from .models import UserSub

import datetime
# Create your views here.

def post_list(request):
	return render(request, 'home/main.html')


def allTrack(request):
	tracklists = TrackList.objects.all()
	bsublists=BsubList.objects.all()
	asublists=AsubList.objects.all()

	posts = Post.objects.filter(published_date__lte=timezone.now())

	context= { 'posts' : posts , 'tracklists':tracklists, 'bsublists':bsublists,'asublists':asublists}
	return render(request,'home/allTrack.html',context)

def resultTrack(request):
	users=User.objects.all()
	usersubs=UserSub.objects.all()
	tracklists = TrackList.objects.all()
	bsublists=BsubList.objects.all()
	asublists=AsubList.objects.all()

	context={'users':users,
			 'usersubs':usersubs,
			 'tracklists':tracklists,
			 'bsublists':bsublists,
			 'asublists':asublists,
			 }

	return render(request, 'home/resultTrack.html',context)