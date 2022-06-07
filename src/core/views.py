from typing import Any, Dict, Optional
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    CreateView, 
    DetailView, 
    UpdateView, 
    DeleteView,
    View,
    ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from core.utils import generate_license_number
from .forms import DriverLicenseCreationForm, PlateNumberCreateForm, RegistrationForm
from django.urls import reverse_lazy
from .models import CustomUser, DriversLicense, Notice, PlateNumber


# =================== [ Core ]========================
class Index(ListView):
    template_name = 'core/index.html'
    context_object_name = 'notices'
    model = Notice

class Registration(CreateView):
    template_name = 'core/signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        try:
            context = super().get_context_data(**kwargs)
            context['driver_license'] = DriversLicense.objects.get(user=self.request.user.id).id
        except (DriversLicense.DoesNotExist) as e:
            print(e)
        return context

class Search(TemplateView):
    template_name = 'core/search.html'

    def post(self, *args, **kwargs):
        search_params = self.request.POST.get('search_params')
        search_category =self.request.POST.get('search_category')
        context = {'type' : search_category}

        if search_category == 'plate_number':
            context['data'] = PlateNumber.objects.filter(plate_number=search_params).first()
        elif search_category == 'driver_license':
            context['data'] = DriversLicense.objects.filter(license_number=search_params).first()
        
        # check if no records where found
        print(context)
        if context.get('data') is None:
            context['error'] = f'Records on {search_params} not found'
        return render(self.request, 'core/search.html', context)

class SearchResult(TemplateView):
    template_name = 'core/search_result.html'
    
# ------------ [ Driver's License] ---------
class LicenseListView(LoginRequiredMixin, ListView):
    model = DriversLicense

class LicenseDetail(LoginRequiredMixin, DetailView):
    model = DriversLicense

class CreateLicense(CreateView):
    template_name = 'core/drivers_license_create.html'
    form_class = DriverLicenseCreationForm
    success_url = reverse_lazy('license')

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        form.instance.iss = ""
        form.instance.exp = ""
        form.instance.license_number = generate_license_number(12)
        return super().form_valid(form)

class LicenseUpdate(UpdateView):
    pass


# ----------- [ Plate NUmber ] ------------
class ListPlateNumber(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return PlateNumber.objects.filter(user=self.request.user)

class CreatePlateNumber(LoginRequiredMixin, CreateView):
    form_class = PlateNumberCreateForm
    template_name = 'core/platenumber_create.html'
    success_url: reverse_lazy('list_platenumber')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class PlateNumberDetail(LoginRequiredMixin, DetailView):
    pass

class PlateNumberDelete(LoginRequiredMixin, DeleteView):
    pass



# -------------------- [ Notice ] -----------------
class CreateNotice():
    pass