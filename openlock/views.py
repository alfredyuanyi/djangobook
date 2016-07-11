#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework import status
from openlock.models import *
from openlock.imageserializers import *
import threading
import time
import socket
import base64
# Create your views here.
image = imagestore(imagePath = 'auto_now_add', imageName = '')


serverHost = '127.0.0.1'
serverPort = 8883

class TestThread(threading.Thread):
	def __init__(self, name,):
		super(TestThread, self).__init__()
		self.name = name
		self.stoped = False
		# self.timeout = timeout
		pass
	
	def run(self):
		def son():
			print 'server is working now!\n'
			server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			server.bind((serverHost, serverPort))
			server.listen(5)
			# server2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# server2.bind(('127.0.0.1', 9990))
			# server2.listen(5)
			while True:
				connect, addr = server.accept()
				connect2, addr2 = server.accept()
				print 'Connected by ',addr
				print 'Connected by ', addr2
				while True:
					data = connect.recv(1024)
					print data
					try:
						connect2.sendall(data)
						pass
					except Exception, e:
						connect2.close()
						# connect.close()
						print 'connect2 closed!'
						print 'connect1 closed!'
						return;
					pass				
				
				print 'closed!'
				pass
			pass
		test = threading.Thread(target = son, args = ())
		test.setDaemon(True)
		test.start()
		
		while  not self.stoped:
			test.join()
			pass

		print 'main thread stoped!'
		pass
	def stop(self):
		
		self.stoped = True
		pass
	pass
#接收图片的socket服务端，将接收到的图片保存到imagePath中去
def imagesocket(host = '127.0.0.1', port = 7000, imagePath = '/iamges/test.jpg'):
	host = '127.0.0.1'
	port = 7000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(5)
	flag = False
	f = open(imagePath, 'wb')
	connect, addr = s.accept()
	while not flag:
		data = connect.recv(1024)
		if len(data) == 0:
			flag = True
			pass
		else:
			data = base64.b64decode(data)
			print data
			f.write(data)
		pass
	f.flush()
	f.close()
	connect.close()
	pass


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
#新用户拍张照片上传到服务器请求注册，服务器获取参数imageName，保存到openlock/images/imageName，
#把该图片的相对路径和图片名保存到数据库中
#参数：imageName
#http方法：GET
#注册成功则返回{'status': '1'}，反之返回{'status': '0'}
def newuser(request):
	if request.method == 'GET':
		defaultPath = 'openlock/images/'
		# defaultPath = ''
		imageName = request.GET['imageName']
		imagePath = defaultPath + imageName
		imagesocket(host = '127.0.0.1', port = 7000, imagePath = imagePath)
		image = imagestore(imagePath = imagePath, imageName = imageName)
		image.save()
		data = {'status': '1'}
		return JSONResponse(data, status = 201)
		pass
	data = {'status': '1'}
	return JSONResponse(data, status = 400)
	pass
#妈的，智障，摄像头上传视频开锁，怎么撸？
def cameraLock():
	pass
#用户请求实时视频，此方法开启多线程获取摄像头上传的数据，并转发给app，获取和转发方式都是socket，
#当用户断开socket连接时，服务器与摄像头的socket连接也自动断开，只用当用户请求实时视频时，服务器才与摄像头建立socket连接
#http方法：GET
#注册成功则返回{'status': '1'}，反之返回{'status': '0'}
def startThread(request):
	if request.method == 'GET':
		global testthread
		testthread = TestThread(name = 'hha')
		testthread.start()
		data = {'status': '1'}
		return JSONResponse(data, status = 201)
		pass
	data = {'status': '0'}
	return JSONResponse(data, status = 400)
	pass
def stopthread(request, timeout = 1.0):
	# global testthread
	# testthread.timeout = timeout
	if request.method == 'GET':
		time.sleep(timeout)
		testthread.stop()
		data = {'status': '1'}
		return JSONResponse(data, status = 201)
	data = {'status': '0'}
	return JSONResponse(data, status = 400)
	pass
#用户输入密码请求开锁，服务器对比数据库中的数据，一致则与锁建立socket连接，并发送'1’给锁，反之返回{'status': '0'}给app
#socket参数： host = '127.0.0.1' port = 9000
def pwdLock(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		pwd = data['pwd']
		print pwd
		try:
			realpwd = lockpwd.objects.get(pwd = pwd)
			flag = '1'
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('192.168.200.102', 9002))
			s.listen(5)
			connect, addr = s.accept()
			connect.sendall(flag)
			connect.close()
			data = {'status': '1'}
			return JSONResponse(data, status = 201)
			pass
		except lockpwd.DoesNotExist:
			data = {'status': '0'}
			return JSONResponse(data, status = 401)
		
		pass
	data = {'status': '0'}
	return JSONResponse(data, status = 400)
	pass
def NewUser(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		if User.objects.filter(userId = data['userId']).count() > 0:
			return JSONResponse(data, status = 400)
			pass
		userId = data['userId']
		pwd = data['pwd']
		userpwd = data['userpwd']
		newuser = User(userId = userId, pwd = pwd, userpwd = userpwd)
		newuser.save()
		return JSONResponse(data, status = 201)
		pass
	return JSONResponse({}, status = 401)
	pass
def user(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		if User.objects.filter(userId = data['userId']).count() > 0:
			return JSONResponse(data, status = 201)
			pass
		return JSONResponse(data , status = 401)
		pass
	return JSONResponse(data, status = 400)
	pass
