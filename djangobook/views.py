# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context


import datetime
# Create your views here.

def Hello(request):
	now = datetime.datetime.now()
	now = (str(now)).split('.')[0]
	html = "<html><body><p>hello world!</p><p>It is now %s.</p></body></html>" % now
	return HttpResponse(html)
	pass
def HoursAhead(request, offset):
	try:
		offset = int(offset)
		pass
	except ValueError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	dt = (str(dt)).split('.')[0]
	html = "<html><body><p>In %s hour(s),it will be %s.</p></body></html>" % (offset,dt) 
	return HttpResponse(html)
	pass
def Home(request):
	# t = get_template('home.html')
	# html = t.render(Context({'name': '晴天'}))
	# return HttpResponse(html)
	return render(request, 'home.html', {'name': '晴天'})
	pass
def ShowRequestMeta(request):
	values = request.META.items()
	values.sort()
	return render(request, 'showrequestMeta.html', {'values': values})
	pass