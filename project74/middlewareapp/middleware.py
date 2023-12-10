from django.http import HttpResponse

class MiddlewareappConfig(object):
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		data = '<h1>Server is under maintainance, please re-visit our server after couple of hours</h1>'
		return HttpResponse(data)