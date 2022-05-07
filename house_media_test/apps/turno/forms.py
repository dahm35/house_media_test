from django import forms
from .models import Turno

class TurnoForm(forms.ModelForm):
    
    class Meta:
        model = Turno
        fields = ('numero_turno','usuario')
