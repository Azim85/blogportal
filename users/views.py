from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from project.decorators import anonymous_required

@anonymous_required('main:index')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

@anonymous_required('main:index')
def login_check(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('main:index')
        
    form = LoginForm()
    return render(request, 'users/login.html', {'form':form})

def logout_check(request):
    logout(request)
    return redirect('main:index')
