# coding: utf8
from django.contrib import admin
from djangobook.models import *
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	#指定可排序
	list_display = ('first_name', 'last_name', 'email')
	#添加搜索栏,并只可搜索一下字段
	search_fields = ('first_name', 'last_name')
	pass

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	#添加过滤器
	list_filter = ('publication_date','title')
	#过滤时间的另一种方式
	date_hierarchy = 'publication_date'
	#自定义排序顺序
	ordering = ('-publication_date',)
	#自定义编辑表单，author表明，元组里的字段必须是Book类中已经定义的字段
	fields = ('title', 'author', 'publisher', 'publication_date')
	#选择多项
	filter_horizontal = ('author',)
	#变下拉框为文本框
	raw_id_fields = ('publisher',)
	pass
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)