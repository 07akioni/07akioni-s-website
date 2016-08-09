from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_),
    url(r'^login/$', views.login_),
    url(r'^logout/$', views.logout_),
    url(r'^login/verify/$', views.verify),
    url(r'^register/$', views.register),
    url(r'^register/newuser/$', views.newuser),
]
