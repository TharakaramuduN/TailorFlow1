from django.shortcuts import render, redirect
from .forms import CreateTailorForm, TailorLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.urls.conf import 

# Create your views here.

def register(request):
    form = CreateTailorForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password1']
        form = CreateTailorForm(request.POST)
        if form.is_valid():
            tailor = form.save()
            user = authenticate(request,username=username,password=password)
            login(request,user)
            return redirect('/')
    return render(request,'tailors/registration.html',context={'form':form})


def tailor_login(request):
    form = TailorLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            # Redirect to a success page or do something else
            return redirect('/')
        else:
            # Handle authentication failure (e.g., show an error message)
            return render(request, 'tailors/login.html', {'error_message': 'Invalid credentials','form':form})
    return render(request,'tailors/login.html',{'form':form})

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        logout(request)
        return redirect(tailor_login)
    return render(request,'tailors/profile.html',context={'user':user})

