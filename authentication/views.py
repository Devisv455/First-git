from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['Pwd']
        Re_password = request.POST["RePwd"]
        
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('home')
        else:
            My_user = User.objects.create_user(username = username, password = password)
        
        
        My_user.save()
        
        messages.success(request, "Thank you for your patronage")
        
        return redirect('signin')
        
    return render(request,"authentication/signup.html")

def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['Pwd']
        
        user = authenticate(username = username, password = password)
    
        if user is not None:
            login(request,user)
            # fname = user.first_name
            return render(request,"authentication/index.html")
        
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def buy(request):
    return render(request,"authentication/buy.html")

def confirm(request):
    return render(request,"authentication/confirm.html")