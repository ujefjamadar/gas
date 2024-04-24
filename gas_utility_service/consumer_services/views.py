from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from consumer_services.models import *
from django.contrib import messages
from .models import ServiceRequest
from django.utils import timezone


@login_required(login_url='/')
def home(request):

    return render(request,'servicereq.html')

def track(request):
    return render(request,'track.html')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        n = request.POST['username']
        p = request.POST['password']
        
        if not n or not p:
            # If username or password is empty, show an error message
            messages.error(request, 'Please enter both username and password.')
            return redirect('/')
        
        user = authenticate(username=n, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('/')
        
def user_logout(request): 
    logout(request)

    return redirect('/')


@login_required(login_url='/')
def submit_service_request(request):
    if request.method == 'POST':
        # Retrieve form data from request.POST
        type_of_request = request.POST.get('type_of_request')
        details = request.POST.get('details')
        files = request.FILES.get('files')

        # Create and save ServiceRequest instance
        service_request = ServiceRequest.objects.create(
            type_of_request=type_of_request,
            details=details,
            submission_date=timezone.now(),
            customer=request.user,
            files=files
        )
        service_request.save()
        # Redirect to a confirmation page
        return redirect('/servicepage')

    return render(request, '/home')

from django.shortcuts import render
from .models import ServiceRequest

def view_service_requests(request):
    # Retrieve all service requests from the database
    service_requests = ServiceRequest.objects.all()

    # Pass the service_requests variable to the template context
    context = {
        'service_requests': service_requests
    }

    # Render the template with the context
    return render(request, 'track.html', context)
