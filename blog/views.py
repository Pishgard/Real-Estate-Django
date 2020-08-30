from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def BlogView(request):
    return HttpResponse('<h1>Blog page</h1>')

def BlogPost(request, id):
    return HttpResponse('<h1>post number:</h1>'+str(id))