from django import forms 
from .models import Topico,Entrada

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['texto']
        labels = {'texto':''}

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['texto']
        labels = {'texto':''}
        widgets = {'texto': forms.Textarea(attrs={'cols':80})}