from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    
    class Meta:
        model = Mensaje  # Asegúrate de que el modelo se llame 'Mensaje' correctamente
        fields = ['receiver', 'content']  # No pongas el espacio extra en 'receiver'
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),  # Asegúrate de que 'receiver' esté bien referenciado
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'receiver': 'Destinatario',  # Cambié 'recipient' por 'receiver' aquí también
            'content': 'Mensaje',
        }

