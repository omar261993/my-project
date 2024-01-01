from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
# Create your views here.

def index(request):
    
        
        
    
    context={'category':Category.objects.all(),'games':Game.objects.all()}
    return render(request,'pages/index.html',context)
def product_details(request,id):
    
    context={'category':Category.objects.all(),'games':Game.objects.all(),'game_id':Game.objects.get(id=id)}
    return render(request,'pages/product-details.html',context)
def shop(request):
    context={'category':Category.objects.all(),'games':Game.objects.all()}
    return render(request,'pages/shop.html',context)
def contact(request):
    context={'category':Category.objects.all(),'games':Game.objects.all()}
    return render(request,'pages/contact.html',context)


def user_login (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('/')
    else:
        form = LoginForm()
    
    context={'category':Category.objects.all(),'games':Game.objects.all(),'form':form}
    return render(request,'pages/login.html',context)

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'pages/signup.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('login')