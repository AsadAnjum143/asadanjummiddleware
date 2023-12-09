from django.shortcuts import render
from django.http import HttpResponse

def creating_middle(request):
	data = '<h1>Hello Welcome to middle ware</h1>'
	return HttpResponse(data)