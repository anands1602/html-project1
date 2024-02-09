from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'home.html')

def department_fun(request):
    dict_dept ={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def docs_fun(request):
    dict_docs = {
        'doc' : Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)


def booking_fun(request):
    if request.method == "POST":
        form = BookingsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingsForm()
        
    dict_form ={
                'form' : form

        }
    return render(request,'booking.html', dict_form)

def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('loginpage')
    return render(request,'signup.html')



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            # return HttpResponse("LOGGED")
            return redirect("homepage")
        else:
            return redirect("signuppage")
    return render(request,'login.html')
    
