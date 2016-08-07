from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin) :
    list_display = ('body', 'timestamp')

# Register your models here.
admin.site.register(Comment, CommentAdmin)
