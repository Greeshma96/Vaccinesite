from django.shortcuts import render,redirect
from .models import Register
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate
# Create your views here.
def index(request):
    return render(request,'nav.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            user=User.objects.create_user(username=username,first_name=first_name,password=password)
            user.save()
            print("usercreated")
        else:
            return redirect('/login/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        user=auth.authenticate(username=username,password=password,confirm_password=confirm_password)
        #if user is not None:
        if password==confirm_password:
            auth.login(request,user)
            return redirect('/booking/')
    return render(request,'login.html')

def booking(request):
    return render(request,'booking.html')

def details(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        place=request.POST.get('place')
        contact_number=request.POST.get('contact_number')
        vaccines_taken=request.POST.get('vaccines_taken')
        allergies=request.POST.get('allergies')
        return redirect('/final/')
    return render(request,'demo.html')

def final(request):
    return render(request,'final.html')

def logout(request):
    return HttpResponse('you are logged out')
    

# if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user.is_authenticated:
#             return redirect('/booking/')
#         else:
#             print('register')
#     return render(request,'login.html')


    # if request.method=="POST":
    #     username=request.POST.get('username')
    #     age=request.POST.get('age')
    #     place=request.POST.get('place')
    #     contact_number=request.POST.get('contact_number')
    #     password=request.POST.get('password')
    #     reg=Register(username=username,age=age,place=place,contact_number=contact_number,password=password)
    #     reg.save()
    #     return redirect('/login/')
    # return render(request,'register.html')