from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserChageForm, CustomUserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.


class SignupView(CreateView):
    model = get_user_model()
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm


class ProfileView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = "accounts/profile.html"
    form_class = CustomUserChageForm
    
    def test_func(self):
        user = self.get_object()
        return user == self.request.user
        
    
