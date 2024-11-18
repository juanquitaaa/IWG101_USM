from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    apodo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=128)  
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

class Mensaje(models.Model):
    contenido = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)