from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('identificacion', 'username', 'nombres', 'apellidos', 'celular', 'is_staff', 'foto')