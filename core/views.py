from django.http import HttpResponse
from django.shortcuts import render, resolve_url, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'


class Register(CreateView):
    template_name = 'core/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('core:login')

    def form_valid(self, form) -> HttpResponse:
        form.save()
        user = User.objects.get(username=form.instance.username)
        Profile.objects.create(user=user)
        return super().form_valid(form)
    

class ProfileDetail(TemplateView):
    template_name = 'core/profile.html'


def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user.profile)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            return redirect('core:profile')
        else:
            print(user_update_form.errors)
            print(profile_update_form.errors)

    if request.method == 'GET':
        context = {
            'p_form': ProfileUpdateForm(instance=request.user.profile),
            'u_form': UserUpdateForm(instance=request.user)
        }
        template_name='core/profile_update.html'
    return render(request, template_name, context)

