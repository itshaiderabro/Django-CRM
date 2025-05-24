from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home.html', {'records': records})



   

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

def item_detail(request, item_id):
    try:
        item = Record.objects.get(id=item_id)
    except Record.DoesNotExist:
        messages.error(request, 'Item not found.')
        return redirect('home')

    return render(request, 'item_detail.html', {'customer_record': item})

def item_delete(request, item_id):
    try:
        item = Record.objects.get(id=item_id)
        item.delete()
        messages.success(request, 'Item deleted successfully.')
    except Record.DoesNotExist:
        messages.error(request, 'Item not found.')

    return redirect('home')

def item_update(request, item_id):
    if request.method == 'POST':
        item = Record.objects.get(id=item_id)
        form = AddRecordForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully.')
            return redirect('item_detail', item_id=item.id)
    else:
        form = AddRecordForm(instance=Record.objects.get(id=item_id))
    return render(request, 'item_update.html', {'form': form, 'item_id': item_id})

def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, 'Record added successfully.')
            return redirect('home')
    else:
        form = AddRecordForm()
    return render(request, 'addRecord.html', {'form': form})

