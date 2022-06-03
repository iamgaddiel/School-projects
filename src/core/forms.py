from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import CustomUser, DriversLicense, PlateNumber



class RegistrationForm(UserCreationForm, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


# ========================= [ Driver's License ] =====================
class DriverLicenseCreationForm(forms.ModelForm):
    class Meta:
        model = DriversLicense
        fields = '__all__'

class PlateNumberCreateForm(forms.ModelForm):
    class Meta:
        model = PlateNumber
        exclude = ['user', 'status']

