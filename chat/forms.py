from django import forms
from .models import Chat



class ChatCreationForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']