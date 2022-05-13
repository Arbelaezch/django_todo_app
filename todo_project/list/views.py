from django.shortcuts import render
from django.http import HttpResponse


# Home page
def index(request):
	return HttpResponse("Hello, world. You're at the list index.")