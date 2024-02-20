from django.shortcuts import render, redirect
from .forms import CreateTailorForm, TailorLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.urls.conf import 
from .models import TailorUser

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = CreateTailorForm()
    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password1']
        form = CreateTailorForm(request.POST,request.FILES)
        if form.is_valid():
            tailor = form.save()
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('/')
    return render(request,'tailors/registration.html',context={'form':form})


def tailor_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    next_url = request.GET.get('next','')
    form = TailorLoginForm()
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('/')
        else:
            # Handle authentication failure (e.g., show an error message)
            return render(request, 'tailors/login.html', {'error_message': 'Invalid credentials','form':form})
    return render(request,'tailors/login.html',{'form':form,'next':next_url})

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        return redirect(tailor_login)
    return render(request,'tailors/profile.html',context={'user':user})

