# coding: utf8
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100) # 指定最大长度
	#email = forms.EmailField(required = False) # 指定该字段为非必需
	email = forms.EmailField(required = False, label = "Your e-mail address")
	message = forms.CharField(widget = forms.Textarea) # widget这个部件表现“显示逻辑”


	pass