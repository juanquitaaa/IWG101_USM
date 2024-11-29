from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CrearUsuario, EditarPerfilForm
from .models import Usuario, Mensaje, Avisos
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
            request.session['usuario_id'] = user.usuario_id
            return redirect('test')  # Redirigir a la página deseada en caso de éxito
        except Usuario.DoesNotExist:
            # Si el usuario no existe o la contraseña es incorrecta, redirigir 6a error
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

    usuario_id = request.session.get('usuario_id')
    usuario = get_object_or_404(Usuario, usuario_id=usuario_id)


    mensajes = Mensaje.objects.all().order_by('-fecha_publicacion')
    avisos = Avisos.objects.all().order_by('-fecha_publicacion')
    return render(request, "web_UDI/test.html", {"mensajes": mensajes, "avisos": avisos,"usuario": usuario})

def error(request):
    return render(request, "web_UDI/error.html")

def posting(request):
    if request.method == "POST":
        contenido = request.POST.get("contenido")
        apodo = request.POST.get("apodo")
        
        try:
            usuario = Usuario.objects.get(apodo=apodo)
            nuevo_mensaje = Mensaje(contenido=contenido, usuario=usuario)
            nuevo_mensaje.save()
            return redirect('test')
        except Usuario.DoesNotExist:
            return render(request, 'web_UDI/posting.html', {"error": "Usuario no encontrado"})

    return render(request, 'web_UDI/posting.html')

def delete(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id)
    mensaje.delete()  # Permite eliminar sin validar usuario
    return redirect('test')  # Redirige de vuelta a la página principal

def crear_aviso(request):
    if request.method == 'POST':
        usuario_nombre = request.POST.get('usuario')
        aviso_texto = request.POST.get('aviso')
        ubicacion = request.POST.get('ubicacion')

        # Validación básica
        if not usuario_nombre or not aviso_texto or not ubicacion:
            return render(request, 'crear_aviso.html', {
                'error': 'Todos los campos son obligatorios.',
            })
        
        try:
            # Buscar el usuario por nombre
            usuario = Usuario.objects.get(apodo=usuario_nombre)
            # Crear el aviso
            Avisos.objects.create(
                usuario=usuario,
                aviso=aviso_texto,
                ubicacion=ubicacion
            )
            return redirect('test')  # Redirigir a una página de lista de avisos
        except Usuario.DoesNotExist:
            # Si el usuario no existe, mostrar un error
            return render(request, 'crear_aviso.html', {
                'error': 'El usuario ingresado no existe. Verifique el nombre.',
            })
    
    # Renderizar el formulario para GET
    return render(request, 'web_UDI/avisos.html')

def settings(request):
    # Recuperamos el usuario_id desde la sesión
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('index')  # Redirige si no hay usuario en sesión

    # Obtenemos al usuario usando el usuario_id
    usuario = get_object_or_404(Usuario, usuario_id=usuario_id)

    # Cargamos el formulario con los datos del usuario
    form = EditarPerfilForm(instance=usuario)

    return render(request, 'web_UDI/settings.html', {'form': form, 'usuario': usuario})

def actualizar_perfil(request, usuario_id):
    # Obtenemos al usuario usando el usuario_id
    usuario = get_object_or_404(Usuario, usuario_id=usuario_id)

    if request.method == 'POST':
        # Creamos el formulario con los datos enviados
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()  # Guardamos los cambios
            return redirect('settings')  # Redirigimos a la página de configuración
    else:
        # Si no es un POST, cargamos el formulario de nuevo
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'web_UDI/settings.html', {'form': form, 'usuario': usuario})