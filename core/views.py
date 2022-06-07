from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import UserCreationForm
from .models import Profile


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'


class Register(CreateView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('core:login')

    def form_valid(self, form) -> HttpResponse:
        user = User.objects.get(username=form.instance.username)
        Profile.objects.create(user=user)
        return super().form_valid(form)
