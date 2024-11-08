from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CrearUsuario
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        email = request.POST.get('Email')  #Dice usuario, porque así estaba en el html y no lo quise mover
        password = request.POST.get('Contraseña') # La variable declarada

        # Verificar si existe un usuario con el email y la contraseña proporcionados
        try:
            user = Usuario.objects.get(email=email, contraseña=password) #es .get(llave_del_modelo=variable declarada)
            # Credenciales válidas
            return redirect('test')  # Redirigir a la página deseada en caso de éxito
        except Usuario.DoesNotExist:
            # Si el usuario no existe o la contraseña es incorrecta, redirigir a error
            return redirect('error')

    return render(request, "web_UDI/index.html")

def register(request):
    if request.method == 'GET':
        return render(request, 'web_UDI/register.html', {
            'form':CrearUsuario()
        })
        #muestro la interfaz
    else:
        Usuario.objects.create(nombres=request.POST['nombres'],
        apellidos=request.POST['apellidos'],
        apodo=request.POST['apodo'],
        email=request.POST['email'],
        contraseña=request.POST['contraseña'],
        foto_de_perfil=request.FILES['foto_de_perfil'])
        return redirect('index')

def test(request):
    return render(request, "web_UDI/test.html")

def error(request):
    return render(request, "web_UDI/error.html")