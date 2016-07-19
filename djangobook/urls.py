# coding: utf8
from django.conf.urls import url, patterns
from django.contrib.auth.views import login,logout
from djangobook import views


urlpatterns = [
	# url(r'^djangobook/hello$', views.Hello),
	#传递额外的参数到视图
	url(r'^$', views.Hello, {'template_name': 'template2'}),
	url(r'^djangobook/time/plus/(\d{1,2})/$', views.HoursAhead),
	url(r'^djangobook/home/$', views.Home),
	url(r'^djangobook/requestmeta/$', views.ShowRequestMeta),
	url(r'^djangobook/contact/$', views.Contact),
	url(r'^djangobook/contact/thanks/$', views.Thanks),
	url(r'^djangobook/requestcontext/$', views.RequestContext),
	url(r'^djangobook/account/login/$', login),
]
urlpatterns += patterns('', 
	#传递额外的参数到视图
	(r'djangobook/hello/$', views.Hello, {'template_name': 'template1'}),
	)
