from django.shortcuts import render

# Create your views here.

def profile(request):
    user = request.user
    return render(request,'profile/profile.html',context={'user':user})