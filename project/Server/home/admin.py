from django.contrib import admin
from .models import TrackList
from .models import BsubList
from .models import AsubList
from .models import Post
from .models import User
from .models import UserSub
# Register your models here.


admin.site.register(User)
admin.site.register(UserSub)

class TrackListadmin(admin.ModelAdmin):
    list_display = ['tname', 'tnum']
    list_filter = [('tname', admin.ChoicesFieldListFilter)]

class BsubListadmin(admin.ModelAdmin):
    list_display = ['bname', 'tnum']
    list_filter = [('tnum')]

class AsubListadmin(admin.ModelAdmin):
    list_display = ['aname', 'tnum']
    list_filter = [('tnum')]

admin.site.register(BsubList, BsubListadmin)
admin.site.register(AsubList, AsubListadmin)
admin.site.register(TrackList, TrackListadmin)
admin.site.register(Post)