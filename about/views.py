from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost
from django.views.decorators.clickjacking import xframe_options_exempt
import math

# Create your views here.
def aboutPage(request) :
    context = {}
    return render(request, 'AboutPage.html', context)
