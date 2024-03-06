from django.shortcuts import render, redirect
from .models import DonationRequest
from .forms import DonationRequestForm

def index(request):
    # Add your view logic here
    return render(request, 'index.html')

def donation_requests(request):
    # Retrieve all donation requests from the database
    donation_requests = DonationRequest.objects.all()
    return render(request, 'donation_request_list.html', {'donation_requests': donation_requests})

def create_donation_request(request):
    if request.method == 'POST':
        # If the form is submitted, process the form data
        form = DonationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_requests')
    else:
        # If it's a GET request, display an empty form
        form = DonationRequestForm()
    return render(request, 'create_donation_request.html', {'form': form})

def user_profile(request):
    # Add your user profile view logic here
    return render(request, 'user_profile.html')
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create a new user account
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            # Redirect to login page or any other page
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})