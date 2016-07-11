from django.conf.urls import url, patterns
from djangobook import views

urlpatterns = [
	url(r'^djangobook/hello$', views.Hello),
	url(r'^$', views.Hello),
	url(r'^djangobook/time/plus/(\d{1,2})/$', views.HoursAhead),
	url(r'^djangobook/home/$', views.Home),
	url(r'^djangobook/requestmeta/$', views.ShowRequestMeta),

]