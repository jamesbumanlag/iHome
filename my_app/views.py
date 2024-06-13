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
            
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, f"You Have Successfully Registered! Welcome! {username}")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'login/register.html', {'form':form})

	return render(request, 'login/register.html', {'form':form})


    

def residents(request):
    if request.user.is_authenticated:
        # Look up records
        records = Record.objects.all()
        return render(request, 'login/residents.html',{'records':records})
    else:
         messages.success(request, 'You must be logged in')
         return redirect('home')





    # # Check to see if logging in
    # if request.method == 'POST':
    #      username = request.POST['username']
    #      password = request.POST['password']

    #      # Authenticate
    #      user = authenticate(request, username=username, password=password)
    #      if user is not None:
    #           login(request, user)
    #           messages.success(request, "You have been logged in")
    #           return redirect('residents')
    #      else:
    #           messages.success(request, 'Error Logging In')
    #           return redirect('home')
    # else:
         
    #      return render(request, 'login/residents.html',{'records':records})

def add_res(request):
    return render(request, 'login/add_res.html')