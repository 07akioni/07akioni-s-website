from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.labHomePage),
    url(r'^(?P<page_index>[0-9]+)$', views.labPage),
    url(r'^[0-9]+/P(?P<id_index>[0-9]+)$', views.postPage),
]
