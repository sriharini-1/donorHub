# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donation-requests/', views.donation_requests, name='donation_requests'),
    path('create-donation-request/', views.create_donation_request, name='create_donation_request'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('signup/', views.signup, name='signup'),
]

