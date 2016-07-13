# coding: utf8
from django.template import RequestContext

def custom_proc(request):
	return {
	'app': 'djangobook',
	'user': request.user,
	'ip_address': request.META['REMOTE_ADDR']
	}
	pass