from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserChageForm, CustomUserCreationForm

# Create your views here.


class SignupView(CreateView):
    model = get_user_model()
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    
    
