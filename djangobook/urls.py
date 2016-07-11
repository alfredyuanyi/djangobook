from django.conf.urls import url, patterns
from djangobook.views import *

urlpatterns = [
	url(r'^djangobook/hello$', Hello),
	url(r'^$', Hello),
	url(r'^djangobook/time/plus/(\d{1,2})/$', HoursAhead),
	url(r'^djangobook/home/$', Home),
	url(r'^djangobook/requestmeta/$', ShowRequestMeta),

]