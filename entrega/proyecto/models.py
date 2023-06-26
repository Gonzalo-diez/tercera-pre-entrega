from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    autor = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.autor.username

class Publicacion(models.Model):
    OPCIONES_PRODUCTOS = [
        ('consola', 'Consola'),
        ('Celular', 'Celular'),
        ('computadora', 'Computadora')
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    producto = models.CharField(max_length=15, choices=OPCIONES_PRODUCTOS, default='consola')
    marca = models.CharField(max_length=40, default='Sin marca')
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField(default='example@example.com')
    imagenProducto = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    comentario = models.ForeignKey(Publicacion, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40, default='Valor predeterminado')
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)


