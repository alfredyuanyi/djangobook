# coding: utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.mail import send_mail
from djangobook.forms import ContactForm
from tutorial.settings import EMAIL_HOST_USER
from functions import *


import datetime
# Create your views here.

def Hello(request, template_name):
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
def Contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cleaned_data = form.cleaned_data
			send_mail(
				cleaned_data['subject'], 
				cleaned_data['message'], 
				from_email = EMAIL_HOST_USER, 
				recipient_list = [cleaned_data['email']]
				)
			return HttpResponseRedirect('/djangobook/contact/thanks/')
			pass
		pass
	else:
		form = ContactForm(initial = {'subject': 'I love your site!'})
	return render(request, 'contact.html', {'form': form})
	pass
def Thanks(request):
	return render(request, 'thanks.html')
	pass
# def ip_address_processor(request):
#     return {'ip_address': request.META['REMOTE_ADDR']}
# def RequestContext(request):
#     c = RequestContext(request, {
#         'foo': 'bar',
#     }, [ip_address_processor])
#     return HttpResponse(t.render(c))
#     pass

# # 简单的登陆
# def login(request):
# 	if request.method != 'POST':
# 		raise Http404('Only POSTs are allowed!')
# 		pass
# 	try:
# 		m = Member.objects.get(username = request.POST['username'])
# 		if m.password == request.POST['password']:
# 			request.session['member_id'] = m.id
# 			return HttpResponseRedirect('/you-are-logged-in/')
# 			pass
# 		pass
# 	except Member.DoesNotExist:
# 		return HttpResponse("You username and password didn't match.")
# 	pass
# # 退出登陆
# def logout(request):
# 	try:
# 		del request.session['member_id']
# 		pass
# 	except KeyError:
# 		pass
# 	return HttpResponse('you are logged out.')
# 	pass

# 设置测试Cookies
# def login(request):
# 	# if we submitted the form...
# 	if request.method == 'POST':
# 		# Check that the test cookie worked (we set it below):
# 		if request.session.test_cookie_worked():
# 			# The test cookie worked, so delete it.
# 			request.session.delete_test_cookie()
# 			# In practice, we'd ned some logic to check username/password
# 			# here, but since this is an example...
# 			return HttpResponse("You're logged in.")
# 			# The test cookie failed, so display an error message.If this
# 			# were a real site, we'd want to display a friendlier message.
# 			pass
# 		else:
# 			return HttpResponse("Please enable cookies and try again.")
# 		pass
# 	# If we didn't post, send the test cookie along with the login form.
# 	request.session.set_test_cookie()
# 	return render(request, 'foo/login_form.html')
# 	pass

# 在视图中同时使用 authenticate()和login()
# def login_view(request):
# 	username = request.POST.get('username', '')
# 	password = request.POST.get('password', '')
# 	user = auth.authenticate(username = username, password = password)
# 	if user is not None and user.is_active:
# 		# Correct pasword, and the user is marked "active"
# 		auth.login(request, user)
# 		# Redirect to a success page.
# 		return HttpResponseRedirect('/account/loggedin/')
# 		pass
# 	else:
# 		# Show an error page
# 		return HttpResponseRedirect('/account/invalid/')
# 	pass