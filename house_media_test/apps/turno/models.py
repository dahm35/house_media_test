from django.db import models
from apps.usuario.models import User

class EstadoTurno(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False, unique=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = 'estado_turno'
        verbose_name_plural = 'estados_turno'

class Turno(models.Model):
    id = models.AutoField(primary_key=True)
    numero_turno = models.IntegerField()
    hora_creacion = models.TimeField(auto_now_add=True, auto_now=False)
    #estado = models.CharField(max_length=20, null=True)#Quizás crear una tabla de parámetros
    estado = models.ForeignKey(EstadoTurno, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    usuario_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_staff')
    def __str__(self):
        return str(self.id) + ' - ' + str(self.numero_turno)
    class Meta:
        verbose_name = 'turno'
        verbose_name_plural = 'turnos'
