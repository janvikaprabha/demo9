from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from requests import Response


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request,"invalid user")
            return redirect('login')


    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']

        password = request.POST['password']
        password2 = request.POST['password2']
        user = authenticate(username=username, password=password)

        if password==password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')


            else:

              user=User.objects.create_user(username=username,password=password)
              user.save()


              print("user created")
        else:
            messages.info(request,"password not matched")
            return redirect('register')

        return redirect('login')
    return render(request,"register.html")




def form(request):
    if request.method== 'POST':

        name=request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        # name7=request.POST['name7']
        # name2 = request.POST['name2']
        # name2 = request.POST['name3']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']

        purpose =request.POST['purpose']
        # name4 =request.POST['name4']
        # name5 = request.POST['name5']



        if form is not None:
            messages.success(request, "Data inserted successfully")


        if User.objects.filter(email=email).exists():

             messages.success(request, "Data inserted successfully")

    return render(request,'form.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')