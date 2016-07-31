from django.contrib import admin
from .models import LabPost

# Register your models here.
class LabPostAdmin(admin.ModelAdmin) :
    list_display = ('title', 'timestamp')

# Register your models here.
admin.site.register(LabPost, LabPostAdmin)
