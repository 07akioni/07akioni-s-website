from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost
from django.views.decorators.clickjacking import xframe_options_exempt
import math

address = ""

# Create your views here.
def homePage(request) :
    return HttpResponseRedirect('blog/1')

def blogHomePage(request) :
    return HttpResponseRedirect('1')

def blogPage(request, page_index) :
    pageSet = []
    posts = BlogPost.objects.all()
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
    context = {'posts': posts, 'address' : address + 'blog/' , 'pageSet' : pageSet, 'actPage' : page_index,
                'nextPage' : nextPage, 'prevPage' : prevPage}
    return render(request, 'HomePage.html', context)

def postPage(request, id_index) :
    post = BlogPost.objects.get(id = int(id_index))
    context = {'address' : address + 'blog/', 'post' : post}
    return render(request, 'blogpage.html', context)
