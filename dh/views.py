from django.shortcuts import render, redirect
from .models import DonationRequest
from .forms import DonationRequestForm
from django.contrib.auth.models import User, auth
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
# views.py
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create a new user object but do not save yet
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Optionally, you can do additional operations like sending confirmation emails, etc.
            # After that, redirect to login page or any other page
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})





