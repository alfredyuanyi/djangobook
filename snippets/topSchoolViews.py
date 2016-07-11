from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from snippets.serializers import NewsSerializer, UserSerializer, ConcernDirectionSerializer, SchoolNewsSerializer
from snippets.models import Department, ConcernDirection, User, News, SchoolNews
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dss.Serializer import serializer
from MongoDB_Driver import *

class register(APIView):
	@csrf_exempt
	def post(self, request, format = None):
		serializer = UserSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			department = Department()
			concernDirectionSerializer = ConcernDirectionSerializer
			return Response(department.data, status = status_HTTP_201_CREATE)
			pass
		return Response(serializer.errors, status = status_HTTP_400_BAD_REQUEST)
		pass
	pass


#@csrf_exempt
class login(APIView):	
	#@csrf_exempt
	def post(self, request, format = None):
		userId = request.data["userId"]
		pwd = request.data["pwd"]
		try:
			user = User.objects.get(userId = userId)
			pass
		except User.DoesNotExist:
			raise Http404
		if pwd == user.pwd:
			news = News.objects.all()[0:10]
			serializer = NewsSerializer(news, many = True)
			print serializer.data
			return Response(serializer.data, status = status_HTTP_201_OK)
		return Response(request.data, status = status_HTTP_401_UNAUTHORIZED)
		pass

#@csrf_exempt
class setconcerndirection(APIView):
	#@csrf_exempt
	def getConcernDirectionobject(self, user):
		try:
			concernDirection = ConcernDirection.objects.get(user = user)
			return concernDirection
			pass
		except ConcernDirection.DoesNotExist:
			raise Http404
		pass
	#@csrf_exempt
	def post(self, request, format = None):
		concernDirectionSerializer = ConcernDirectionSerializer(request.data)
		if concernDirectionSerializer.is_valid():
			concernDirectionSerializer.save()
			return Response(concernDirectionSerializer.data, status = status_HTTP_201_CREATE)
			pass
		return Response(concernDirectionSerializer.errors, status = status_HTTP_400_BAD_REQUEST)
		pass
	#@csrf_exempt
	def put(self, request, format = None):
		user = request.data['user']
		concernDirection = getConcernDirectionobject(user)
		serializer = ConcernDirectionSerializer(concernDirection, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status_HTTP_201_OK)
			pass
		return Response(serializer.errors, status = status_HTTP_400_BAD_REQUEST)
		pass


class JsonResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JsonResponse, self).__init__(content,**kwargs)
		pass


def register(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		print User.objects.filter(userId = data["userId"]).count()
		if User.objects.filter(userId = data["userId"]).count() >0:
			return JsonResponse(data, status = 400)
		serializer = UserSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			department = Department()
			department = dict(department.data, **serializer.data)
			print department
			#concernDirectionSerializer = ConcernDirectionSerializer()
			return JsonResponse(department, status = 201)
			pass
		return JsonResponse(serializer.errors, status = 400)
	elif request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many = True)
		return JsonResponse(serializer.data, status = 201)
	return JsonResponse(serializer.errors, status = 400)
	pass

def login(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		userId = data["userId"]
		pwd = data["pwd"]
		print userId,pwd
		try:
			user = User.objects.get(userId = userId)
			pass
		except User.DoesNotExist:
			raise Http404
		if pwd == user.pwd:
			mongoDriver = MongoDB_Driver()
			news = mongoDriver.db_findAll('school_news',{})[0:10]
			data = []
			for n in news:
				del n['_id']
				data.append(n)
			# print data
			# news = News.objects.all()[0:10]
			# serializers = NewsSerializer(news, many = True)
			return JsonResponse(data, status = 201)
		return JsonResponse(data, status = 401)
	pass

def getConcernDirectionobject(user):
		try:
			concernDirection = ConcernDirection.objects.get(user = user)
			return concernDirection
			pass
		except ConcernDirection.DoesNotExist:
			raise Http404
		pass

def setconcerndirection(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		concernDirectionSerializer = ConcernDirectionSerializer(data = data)
		if concernDirectionSerializer.is_valid():
			concernDirectionSerializer.save()
			news = News.objects.all()[0:10]
			serializer = NewsSerializer(news, many = True)
			return JsonResponse(serializer.data, status = 201)
			pass
		return JsonResponse(serializer.errors, status = 400)
		pass
	if request.method == 'PUT':
		data = JSONParser().parse(request)
		user = data['user']
		concernDirection = getConcernDirectionobject(user)
		serializer = ConcernDirectionSerializer(concernDirection, data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)
			pass
		return JsonResponse(serializer.errors, status = 400)
		pass
	pass

def GetNews(host = '127.0.0.1', port = 40029, databaseName = 'test', collection = 'test', condition = {}, num = 10):
	mongoDriver = MongoDB_Driver(host, port, databaseName)
	news = mongoDriver.db_findAll(collection, condition)[0:num]
	data = []
	for n in news:
		n['_id'] = (str)(n['_id'])
		data.append(n)
		pass
	return data
	pass
def test(request):
	if request.method == 'GET':
		# mongoDriver = MongoDB_Driver()
		# news = mongoDriver.db_findAll('school_news',{})[0:10]
		# data = []
		# for n in news:
		# 	n['_id'] = (str)(n['_id'])
		# 	data.append(n)
		data = GetNews(collection = 'school_news', num = 9)
		return JsonResponse(data,status = 201)
	
	pass

