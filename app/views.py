from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'a.html')
def index(request):
    return render(request, 'index.html')


    
