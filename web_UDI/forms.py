from django import forms
from .models import Usuario
from django.forms import TextInput, EmailInput, FileInput
from django.forms.widgets import ClearableFileInput
class CrearUsuario(forms.Form):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    apodo = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=128)  
    foto_de_perfil = forms.ImageField(required=False)
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'apodo', 'email', 'foto_de_perfil']  # Campos editables
class MiFormulario(forms.Form):
    nombres = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    apodo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    # Aquí personalizamos el widget de foto de perfil para quitar el "clear"
    foto_de_perfil = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    )