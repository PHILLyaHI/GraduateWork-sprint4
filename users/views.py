from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import RegisterForm


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserChangeView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

