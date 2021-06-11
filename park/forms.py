from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Parks

class ParkForm(ModelForm):
    class Meta:
        model = Parks
        exclude = ['user']
