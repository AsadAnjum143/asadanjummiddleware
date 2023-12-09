from django.http import HttpResponse

class MiddlewareappConfig(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		data = '<h1>Server is under maintainance</h1>'
		return HttpResponse(data)