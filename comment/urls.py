from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.func),
    url(r'^create/$', views.createComment),
]
