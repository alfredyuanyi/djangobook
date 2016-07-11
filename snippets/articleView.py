from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import TestArticle
from snippets.serializers import TestArticleSerializer
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

class ArticleJsonResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(ArticleJsonResponse, self).__init__(content, **kwargs)
		pass

@csrf_exempt
def articleList(request):
	if request.method == 'GET':
		TestArticles = TestArticle.objects.all()
		print TestArticles
		serializers = TestArticleSerializer(TestArticles, many = True)
		return ArticleJsonResponse(serializers.data)
		pass		
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TestArticleSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return ArticleJsonResponse(serializer.data, status = 201)
			pass
		return ArticleJsonResponse(serializer.errors, status = 400)
@csrf_exempt
def articleDetail(request):
	try:
		href = request.GET['href']
		article = TestArticle.objects.filter(href = href)
		pass
	except TestArticle.DoesNotExist:
		return ArticleJsonResponse(status = 404)
	if request.method == 'GET':
		serializer = TestArticleSerializer(article, many = True)
		return ArticleJsonResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TestArticleSerializer(article, data = data)
		if serializer.is_valid():
			serializer.save()
			return ArticleJsonResponse(serializer.data)
		return ArticleJsonResponse(serializer.errors, status = 400)
	elif request.method == 'DELETE':
		article.delete()
		return ArticleJsonResponse(status = 204)
	
class article_list(APIView):
	def get(self, request, format = None):
		articles = TestArticle.objects.all()
		serializer = TestArticleSerializer(articles, many = True)
		return Response(serializer.data)
		pass
	def post(self, request, format = None):
		serializer = TestArticleSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status_HTTP_201_CREATE)
		return Response(serializer.errors, status = status_HTTP_400_BAD_REQUEST)
		pass
	pass
class article_detail(APIView):
	def get_article(self, pk):
		try:
			article = TestArticle.objects.get(pk = pk)
			return article
			pass
		except TestArticle.DoesNotExist:
			raise Http404
		pass
	def get(self, request, pk, format = None):
		article = self.get_article(pk)
		serializer = TestArticleSerializer(article)
		return Response(serializer.data)
		pass
	def put(self, request, pk, format = None):
		article = self.get_article(pk)
		serializer = TestArticleSerializer(article, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status_HTTP_400_BAD_REQUEST)
		pass
	def delete(self, request, pk, format = None):
		article = self.get_article(pk)
		article.delete()
		return Response(status = status_HTTP_204_NO_CONTENT)
		pass
