from .models import Provider
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import mysql.connector as sql

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def home(request):
    return render(request, 'home.html')

def marketplace(request):
    return render(request, 'MarketPlace.html')


def signup(request):
    return render(request, 'signup.html')

def insertuser(request):
    Bname = request.POST['business_name']
    StreetNo = request.POST['street_number']
    StreetName = request.POST['street_name']
    City = request. POST['city']
    State = request.POST['state']
    Country = request.POST['country']
    PinCode = request.POST['zip_code']
    Btagline = request.POST['business_tagline']
    Bdescription = request.POST['business_description']

    Username = request.POST['provider_username']
    Name = request.POST['provider_name']
    Email = request.POST['provider_email']
    Mob = request.POST['provider_mobile']
    Password = request.POST['provider_password']
    Website = request.POST['website_link']

    # Create a Provider instance
    pr = Provider(
        business_name=Bname,
        street_number=StreetNo,
        street_name=StreetName,
        city=City,
        state=State,
        country=Country,
        zip_code=PinCode,
        business_tagline=Btagline,
        business_description=Bdescription,
        provider_username=Username,
        provider_name=Name,
        provider_email=Email,
        provider_mobile=Mob,
        provider_password=Password,
        website_link=Website
    )
    pr.save()
    messages.success(request, "Signed up Successfully..")
    return redirect('index')


username=''
pwd=''

def login_view(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="YGunther@2209", database='tradesocial_database')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "username":
                username = value
            if key == "password":
                pwd = value
        
        c = "select * from users where provider_username='{}' and provider_password='{}'".format(username, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            messages.error(request, "Invalid Login Credentials..")
            return render(request, 'login.html')
        else:
            request.session['username'] = username
            messages.success(request, "Logged in Successfully..")
            return redirect('home')  # Use 'redirect' instead of 'render' to handle post/redirect/get pattern

    return render(request, 'login.html')


def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
        messages.success(request, "Logged out Successfully")
    return redirect('index')  # Redirect to index page after logout


def profile_view(request):
    if 'username' not in request.session:
        return redirect('login')
    
    username = request.session['username']
    # Fetch user details from database if necessary

    return render(request, 'profilepage.html', {'username': username})