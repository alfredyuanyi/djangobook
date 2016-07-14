# coding: utf8
# 自定义标签和过滤器
# 如需使用，则需要在模板中写入如下内容：
# {% load poll_extras %}  即与当前文件同名

from django import template

import datetime

# register 为模块级变量，为template.Librar的实例，事所有注册标签和过滤器的数据结构，因此需写在顶部。
register = template.Library()
# *************************************************************************************
# 自定义模板过滤器，使用时： {{ somevariable|cut:" "}}
def Cut(value, arg):
	return value.replace(arg, '')
	pass
def Lower(value):
	return value.lower()
	pass

# 定义完过滤器之后，需要用Library实例来注册它。
register.filter('cut', Cut)
register.filter('lower', Lower)
# 或者可以使用装饰器
# @register.filter(name='cut')
# def Cut(value, arg):
# 	return value.replace(arg, '')
# 	pass

# **************************************************************************************
# 自定义模板标签

# 编写编译函数
def do_current_time(parser, token):
	try:
		tag_name, format_string = token.split_contents()
		pass
	except ValueError:
		msg = '%r tag requires a single argument' % token.split_contents()[0]
		raise template.TemplateSyntaxError(msg)
	return CurrentTimeNode(format_string[1:-1])
	pass
# 编写模板节点
class CurrentTimeNode(template.Node):
	def __init__(self, format_string):
		self.format_string = str(format_string)
		pass
	def render(self, context):
		now = datetime.datetime.now()
		return now.strftime(self.format_string)
		pass
class CurrentTimeNode2(template.Node):
	def __init__(self, format_string):
		self.format_string = str(format_string)
		pass
	def render(self, context):
		now = datetime.datetime.now()
		context['current_time'] = now.strftime(self.format_string)
		return ''
		pass
# 注册标签
register.tag('current_time', do_current_time)
# 使用时可如此：
# {% current_time2 "%Y-%M-%d %I:%M %p" %} <p> The time is {{ current_time }}. </p>

# 分析直至另一个模板标签(该标签不保存内容)
def do_comment(parser, token):
	nodeList = parser.parse(('endcomment',))
	nodeList.delete_first_token()
	return CommentNode()
	pass
class CommentNode(template.Node):
	def render(self, context):
		return ''
		pass
	pass

# 分析直至另一个模板标签并保存内容
def do_upper(parser, token):
	nodeList = parser.parse(('endupper',))
	nodeList.delete_first_token()
	return UpperNode(nodeList)
	pass
class UpperNode(template.Node):
	def __init__(self, nodeList):
		self.nodeList = nodeList
		pass
	def render(self, context):
		output = self.nodeList.render(context)
		return output.upper()
		pass

# 简单标签的快捷方式 (使用register.simple_tag())
def current_time(format_string):
	try:
		return datetime.datetime.now().strftime(str(format_string))
		pass
	except UnicodeEncodeError:
		return ''
	pass
register.simple_tag(current_time)# 或者把register.simple_tag当装饰器直接放在current_time上也可。
