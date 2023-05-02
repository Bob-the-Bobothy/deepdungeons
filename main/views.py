from django.shortcuts import render
from markdown import markdown

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def socials(request):
    return render(request, 'socials.html')

def privacy_policy(request):
    file_path = 'templates/privacy_policy.md'
    with open(file_path, 'r') as f:
        content = f.read()
    html = markdown(content)
    return render(request, 'privacy_policy.html', {'html': html})

def tos(request):
    file_path = 'templates/tos.md'
    with open(file_path, 'r') as f:
        content = f.read()
    html = markdown(content)
    return render(request, 'tos.html', {'html': html})