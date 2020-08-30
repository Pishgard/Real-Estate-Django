from django.shortcuts import render 
from  .models import About

# Create your views here.

def index(request):
    return render(request, template_name='page/index.html')

def about(request):
    abouts = About.objects.all()
    context = {
        'abouts': abouts,
        
    }
    return render(request, template_name='page/about.html', context = context) 