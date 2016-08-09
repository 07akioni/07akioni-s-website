from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def func(request):
    posts = Comment.objects.all().order_by('-timestamp')
    context = {'posts' : posts}
    return render(request, 'CommentPage.html', context)

@login_required
def createComment(request):
    if request.method == 'POST' :
        Comment (
            body=request.POST.get('body'),
            timestamp=datetime.now(),
            username=request.user.username
        ).save()
    return HttpResponseRedirect('/comment/')
