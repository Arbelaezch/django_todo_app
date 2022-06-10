from django.shortcuts import render
from django.http import HttpResponse

from .models import Item, List

# Create your views here.
def home(request):
    list = List.objects.all()

    return HttpResponse("Hello, world!")