from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import LabPost
from django.views.decorators.clickjacking import xframe_options_exempt
import math

address = ""

# Create your views here.

def labHomePage(request) :
    return HttpResponseRedirect('/lab/1')

def labPage(request, page_index) :
    pageSet = []
    posts = LabPost.objects.all()
    sizeOfPosts = len(posts)
    maxPage = int(math.ceil(sizeOfPosts / 5))
    maxPage = max(1, maxPage)
    prevPage = str(int(page_index) - 1)
    if page_index == '1' :
        prevPage = '1';
    midnum = int(page_index)
    for i in range(max(1, midnum - 2), min(midnum + 3, maxPage + 1)) :
            pageSet.append(str(i))
    if maxPage > int(page_index) :
        nextPage = str(1 + int(page_index))
    else :
        nextPage = str(maxPage)
    posts = posts.order_by('-timestamp')[5 * (int(page_index) - 1) : 5 * int(page_index)]
    context = {'posts': posts, 'address' : address + 'lab/' , 'pageSet' : pageSet, 'actPage' : page_index,
                'nextPage' : nextPage, 'prevPage' : prevPage}
    return render(request, 'LabHomePage.html', context)

def postPage(request, id_index) :
    post = LabPost.objects.get(id = int(id_index))
    context = {'address' : address + 'lab/', 'post' : post}
    return render(request, 'LabContentPage.html', context)
