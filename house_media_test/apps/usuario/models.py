from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    identificacion = models.IntegerField('Número de identificación', primary_key=True)
    #Falta username y email
    nombres = models.CharField('Nombres', max_length=50, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=50, blank=True, null=True)
    celular = models.CharField('Número de celular', max_length=15, blank=True, null=True)
    foto = models.ImageField('Foto', upload_to='fotos', blank=True, null=True)

    #USERNAME_FIELD = 'identificacion'
    REQUIRED_FIELDS = ['nombres', 'apellidos']

    class Meta:
        #db_table = 'db_users'
        verbose_name = 'usuario'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return f'{self.nombres} {self.apellidos} - {self.identificacion}'