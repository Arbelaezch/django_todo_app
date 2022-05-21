from django.shortcuts import render
from django.http import HttpResponse


# Home page
def home(request):
	return render(request, 'home.html')

def list(request):
	return render(request, 'list.html')
