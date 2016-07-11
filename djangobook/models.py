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

class Book(models.Model):
	title = models.CharField(max_length = 100)
	author = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.title
		pass
