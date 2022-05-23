from django.shortcuts import render
from django.http import HttpResponse
from .models import List

rooms = [
	{"id": 1, 'name': 'Lets learn python!'},
	{"id": 2, 'name': 'Design with me'},
	{"id": 3, 'name': 'Frontend developer'},

]

# Home page
def home(request):
	item_list = List.objects.all()
	# output = ', '.join([q.text for q in item_list])
	return render(request, 'home.html', {'list':item_list})

def list(request):
	return render(request, 'list.html')
