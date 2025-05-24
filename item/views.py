from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home.html')



   

def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               messages.success(request, 'Registration successful. You are now logged in.')
               return redirect('home')
           else:
               messages.error(request, 'Registration successful but login failed.')
               return redirect('register')
    form = SignUpForm()
   
    return render(request, 'register.html', {'form': form})


