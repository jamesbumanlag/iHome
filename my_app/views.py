from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, PersonalCareForms
from .models import Record, PersonalCare

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
			return redirect('residents')
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



def add_res(request):
    return render(request, 'login/add_res.html')


def cus_record(request,pk):
    if request.user.is_authenticated:
         # Look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'login/record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You need to be logged in to view record')
        return redirect('home')
    
# def add_care(request):
#     form = PersonalCareForms(request.POST or None)
#     if request.user.is_authenticated:
        
#         if request.method == 'POST':
            
#             if form.is_valid():
#                 add_care = form.save()
#                 messages.success(request, 'Saved')
#                 return redirect('residents')
        
#         return render(request, 'login/add_care.html', {'form':form})
    

#     else:
#         messages.success(request, 'Unauthorized Access')
#         return redirect('home')

def add_care(request):
    form = PersonalCareForms(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Added')
                return redirect('residents')
        
        return render (request,'login/add_care.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')
    
    


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added')
                return redirect('residents')
        
        return render (request,'login/add_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged in')
        return render(request, 'login/residents.html')
    
def update_record(request,pk):
    if request.user.is_authenticated:
            # Look up record
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated')
            return redirect('record', pk=current_record.id)
        return render(request, 'login/update_record.html' , {'form':form})
    else:
        messages.success(request, 'You Must Be logged in')
        return redirect('home')

def delete_record(request, pk):
     if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Record has been deleted')
        return redirect('residents')
     else:
        messages.success(request, 'Unauthorized to delete')
        return redirect('residents')