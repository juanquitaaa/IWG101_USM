from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CrearUsuario
from .models import Usuario


# Create your views here.
def index(request):
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
