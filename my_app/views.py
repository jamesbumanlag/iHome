from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def reset(request):
    return render(request, 'login/reset.html')



def navbar(request):
    # User login 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('residents')
        else:
            
            messages.success(request,'Invalid Username and Password')
            return redirect('home')

    else:
        return render(request, 'menu.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username = username, password = password)
            login(request, user)

            messages.success(request, "Registered Successfully")
            return redirect('residents')
    else:
        form = SignUpForm()
        return render(request, 'login/register.html', {'form':form})


    return render(request, 'login/register.html', {'form':form})

def residents(request):
    records = Record.objects.all()
    return render(request, 'login/residents.html', {'records':records})

def add_res(request):
    return render(request, 'login/add_res.html')

def record(request, pk):
    if request.user.is_authenticated:
        # look up record
        res_record = Record.objects.get(id=pk)
        return render(request, 'login/record.html',{'res_record':res_record})
    else:
        messages.success(request, "You Must Be Logged In")
        return redirect('home')