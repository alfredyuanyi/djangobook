from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from openlock import views

urlpatterns = [
	url(r'^lock/home/realtimevideo/$', views.startThread),
	url(r'^lock/home/realtimevideo/stop/$', views.stopthread),
	url(r'^lock/home/pwdlock/$', views.pwdLock),
	url(r'^lock/home/cameralock/$', views.cameraLock),
	url(r'^lock/home/newuser/$', views.NewUser),
	url(r'^lock/home/user/$', views.user),
]

urlpatterns = format_suffix_patterns(urlpatterns)