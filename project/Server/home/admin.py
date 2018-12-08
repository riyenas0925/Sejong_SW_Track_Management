from django.contrib import admin
from .models import Post
from .models import TrackList
from .models import AsubList
from .models import BsubList
# Register your models here.

admin.site.register(Post)
admin.site.register(TrackList)
admin.site.register(BsubList)
admin.site.register(AsubList)