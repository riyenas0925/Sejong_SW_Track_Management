from django.contrib import admin
from .models import Post
from .models import Track
from .models import SubList
# Register your models here.

admin.site.register(Post)
admin.site.register(Track)
admin.site.register(SubList)