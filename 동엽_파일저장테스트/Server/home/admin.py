from django.contrib import admin
from .models import TrackList
from .models import BsubList
from .models import AsubList
from .models import Post
from .models import User
from .models import UserSub
# Register your models here.


admin.site.register(TrackList)
admin.site.register(BsubList)
admin.site.register(AsubList)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(UserSub)