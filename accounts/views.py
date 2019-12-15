from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('home')
        except User.DoesNotExist:
            return render(request, 'login.html', {'error':'username or password is incorrect'})

    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passconfirm']:
            try:    
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error':'Already taken'})
            except User.DoesNotExist:
                user = User.objects.create(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error':'Passwords mismatch'})
    return render(request, 'signup.html')