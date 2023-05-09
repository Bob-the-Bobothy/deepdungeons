from django.shortcuts import render
from markdown import markdown

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def download(request):
    return render(request, 'download.html')

def tos(request):
    return render(request, 'tos.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')