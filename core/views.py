from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.


def index(request):
	subs = Subscribed.objects.all()

	context = {
		'subs' : subs
	}
	return render(request, 'core/home.html', context)