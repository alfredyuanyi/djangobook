# coding: utf8
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Publisher(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 50)
	city = models.CharField(max_length = 60)
	state_province = models.CharField(max_length = 30)
	country = models.CharField(max_length = 50)
	website = models.URLField()
	def __unicode__(self):
		return self.name
		pass
	#指定默认的排序方式
	class Meta:
		ordering = ['name']
	pass

class Author(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 40)
	email = models.EmailField(blank = True)
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name) 
		pass
	pass

# 自定义manager

# 增加额外的Manager方法
# 为Book模型定义一个title_count方法
class BookManager(models.Manager):
	def title_count(self, keyword):
		return self.filter(title__icontains = keyword).count()
		pass

# 修改初始Manager,通过覆盖Manager.get_query_set()方法来重写manager的基本QuerySet。
# 为Book模型添加一个只返回作者时Jack Ma的Manager
class MaBookManager(models.Manager):
	def get_query_set(self):
		return super(MaBookManager, self).get_query_set().filter(author = 'Ma Jack')
		pass

class Book(models.Model):
	title = models.CharField(max_length = 100)
	author = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank = True, null = True)
	# 默认manager   
	#********************************************************************
	# 注意：django 会把第一个Manager定义为默认的Manager，django 的许多部分（不包括admin应用）将会明确地为模型使用这个manager
	#*******************************************************************
	objects = models.Manager()
	# 自定义manager
	title_count = BookManager()
	# 只返回Jack Ma的manager
	JackMa_objects = MaBookManager()
	def __unicode__(self):
		return self.title
		pass

# 模型方法 可以为模型添加行级功能
from django.contrib.localflavor.us.models import USStateField

class Person(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	birth_date = models.DateField()
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 50)
	state = USStateField()

	def baby_boomer_status(self):
		import datetime
		if datetime.date(1945, 8, 1) <= self.birth_date <= datetime.date(1964, 12, 31):
			return 'Baby boomer'
			pass
		if datetime.date(1945, 8, 1) > self.birth_date:
			return 'Pre-boomer'
			pass
		return 'Post-boomer'
		pass
	def is_midwestern(self):
		return self.state in ('IL', 'WI', 'MI', 'IN', 'OH', 'IA', 'MO')
		pass
	def _get_full_name(self):
		return u'%s %s ' % (self.first_name, self.last_name)
	full_name = property(_get_full_name)
		pass

