from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment
from datetime import datetime
# Create your views here.
def func(request):
    posts = Comment.objects.all().order_by('-timestamp')
    context = {'posts' : posts}
    return render(request, 'CommentPage.html', context)

def createComment(request):
    if request.method == 'POST' :
        Comment (
            body=request.POST.get('body'),
            timestamp=datetime.now()
        ).save()
    return HttpResponseRedirect('/comment/')
