from django.shortcuts import render
# Create your views here.


def home(request):
    print(request.user.id)
    return render(request, 'home/home.html', context={'title': 'home'})
