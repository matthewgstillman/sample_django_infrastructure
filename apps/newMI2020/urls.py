from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^courses/$', views.courses, name="courses"),
    url(r'^jobs/$', views.jobs, name="jobs"),
    url(r'^iotdevelopers/$', views.iotdevelopers, name="iotdevelopers"),
    url(r'^courseinfo/$', views.courseinfo, name="courseinfo"),
] 