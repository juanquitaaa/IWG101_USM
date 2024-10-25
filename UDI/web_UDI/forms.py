from django import forms

class CrearUsuario(forms.Form):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    apodo = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    contraseña = forms.CharField(max_length=128)  
    foto_de_perfil = forms.ImageField(required=False)