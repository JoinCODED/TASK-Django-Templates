from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1>Hello, welcome</h1>")



