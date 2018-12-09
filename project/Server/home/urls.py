from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^allTrack/',views.allTrack,name='allTrack'),
]