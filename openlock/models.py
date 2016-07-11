from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
class lockpwd(models.Model):
	pwd = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.pwd
		pass
	pass
# class images(models.Model):
# 	image = models.ImageField(upload_to = '/picture/',max_length = 250)
# 	iamgeName = models.CharField(max_length = 100)
# 	def __unicode__(self):
# 		return self.iamgeName
# 		pass
# 	pass
class imagestore(models.Model):
	imagePath = models.CharField(max_length = 250, blank = True, default = '/images/')
	imageName = models.CharField(max_length = 100, blank = True, default = 'unknow.jpg')
	def __unicode__(self):
		return self.imageName
		pass
	pass
class User(models.Model):
	userId = models.CharField(max_length = 100)
	pwd = models.CharField(max_length = 100)
	userpwd = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.userId
		pass
admin.site.register(User)