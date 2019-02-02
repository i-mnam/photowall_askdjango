# blog/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_id>\d+)/comment/(?P<id>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^(?P<post_id>\d+)/comment/(?P<id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]