from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
   

def index(request):
    return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")
    
def about(request):
    return HttpResponse('Rango says here is the about page. <br/> <a href="/rango/">Index</a>')
