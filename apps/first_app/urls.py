from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add_course$', views.add_course),
    url(r'^courses/(?P<id>\d+)$', views.process),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy)
]
