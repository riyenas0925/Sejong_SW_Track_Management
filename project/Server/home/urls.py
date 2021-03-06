from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^allTrack',views.allTrack, name='allTrack'),
    url(r'^resultTrack',views.resultTrack, name='resultTrack'),
    url(r'^import', views.import_data, name="import"),
    url(r'^handson_view', views.handson_table, name="handson_view"),
    url(r'^test',views.test,name="test"),
    url(r'^notice',views.notice2,name="notice"),
    url(r'^stats',views.trackRate,name="stats"),
]