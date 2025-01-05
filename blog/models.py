from django.db import models
from django.contrib.auth.models import User

# Modelo para los blogs
class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes_blog/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class AcercaDe(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    categoria = models.CharField(max_length=100)  # Campo categoria, debe existir
    destacado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
        
class Entrevista(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    contenido = models.TextField()
    entrevistado = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='entrevistas/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField()
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    categoria = models.CharField(max_length=100)  # Asegúrate de que esta línea esté presente

    def __str__(self):
        return self.titulo  
    
class Analisis(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    contenido = models.TextField()
    autor = models.CharField(max_length=100)  # Autor en lugar de entrevistado
    imagen = models.ImageField(upload_to='analisis/')
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

 # Para la relación con el usuario

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.remitente.username} a {self.receptor.username}"
