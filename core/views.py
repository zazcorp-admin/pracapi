from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
	return HttpResponse("This is just a testing for cyclick")