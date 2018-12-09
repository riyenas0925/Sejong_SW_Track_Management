from django.contrib import admin
from .models import TrackList
from .models import BsubList
from .models import AsubList
# Register your models here.


admin.site.register(TrackList)
admin.site.register(BsubList)
admin.site.register(AsubList)