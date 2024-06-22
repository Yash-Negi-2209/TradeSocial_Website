from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'Home.html')

def marketplace(request):
    return render(request, 'marketplace.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')