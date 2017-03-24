from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^add_course$', views.add ),
    url(r'^courses/destroy/(?P<id>\d+)$', views.remove ),
]
