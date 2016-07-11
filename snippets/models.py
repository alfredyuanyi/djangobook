# coding:utf-8
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

#导入MongoEngine
from mongoengine import *
connect('test',
	host = '127.0.0.1',
	port = 40029)
#Create your models here.
class Info(Document):
	title = StringField(max_length = 100)
	url = StringField(max_length = 100)
	pass
# admin.site.register(Info)

class SchoolNews(models.Model):
	href = models.CharField(max_length = 100)
	title = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.title
		pass
	pass
admin.site.register(SchoolNews)
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('auth.User', related_name = 'Snippets', default = '1	')
    highlighted = models.TextField(default = 'nidayeo')
    def save(self, *args, **kwargs):
    	lexer = get_lexer_by_name(self.language)
    	linenos = self.linenos and 'table' or False
   	options = self.title and {'title': self.title} or {}
    	formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
	self.highlighted = highlight(self.code, lexer, formatter)
	super(Snippet, self).save(*args, **kwargs)
    class Meta:
        ordering = ('created',)
admin.site.register(Snippet)

#test models
class TestArticle(models.Model):
	#created = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 250)
	href = models.CharField(max_length = 100)
	class Meta:
		ordering = ('title',)

admin.site.register(TestArticle)

#registerform
class User(models.Model):
	userId = models.CharField(max_length = 50)
	pwd = models.CharField(max_length = 100)
	email = models.CharField(max_length = 150)
	tel = models.CharField(max_length = 50)
	school = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.userId
		pass
admin.site.register(User)
#concernDirections
class ConcernDirection(models.Model):
	user = models.ForeignKey(User, related_name = "concernDirection")
	officeOfTeachingAffairs = models.IntegerField(default = 0)
	personnelDivision = models.IntegerField(default = 0)
	schoolOfComputing = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.user
		pass
admin.site.register(ConcernDirection)
#news
class News(models.Model):
	newsUrl = models.URLField(max_length = 100)
	title = models.CharField(max_length = 150)
	creatTime = models.DateTimeField(auto_now_add = True)
	class Meta:
		ordering = ('creatTime',)
	def __unicode__(self):
		return self.title
		pass
admin.site.register(News)

class Department(object):
	data = {"0": "8", "1": "教务处", "2": "校长办公室", "4": "发展规划处", "8": "人事处", "16": "学生工作处", "32": "招生就业处", "64": "保卫处", "128": "产业处"}
	pass
#部门信息表
class Branch(models.Model):
	branchId = models.IntegerField(blank = False, default = 0)
	branchName = models.CharField(max_length = 150, blank = False, default = 'unNamedBranch')
	pass
admin.site.register(Branch)
#新设计的用户表，继承自上一次的用户表
class SchoolUser(User):
	topNewsTime = models.DateTimeField()
	bottomNewsTime = models.DateTimeField()
	concernedDirection = models.CharField(max_length = 100, blank = False, default = '000000')
admin.site.register(SchoolUser)
#通知表暂且使用上次定义好的News表

