from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Turno, EstadoTurno
from .forms import TurnoForm

class TurnoList(ListView):
    model = Turno
    template_name='index.html'
    
class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = "crear_turno.html"
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        estado_pendiente = EstadoTurno.objects.get(nombre='Pendiente')
        form.instance.estado = estado_pendiente
        form.instance.usuario_staff = self.request.user
        return super().form_valid(form)

class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = "crear_turno.html"
    success_url = reverse_lazy('index')

class TurnoDeleteView(DeleteView):
    model = Turno
    template_name = "confirmar_eliminacion_turno.html"
    success_url = reverse_lazy('index')

class TurnosPendientesView(ListView):
    model = Turno
    #context_object_name = ''
    template_name='index.html'

    def get_queryset(self):
        estado_pendiente = EstadoTurno.objects.get(nombre='Pendiente')
        turnos_pendientes = self.model.objects.filter(estado=estado_pendiente)
        turnos_pendientes_ordenados = turnos_pendientes.order_by('-hora_creacion')
        ultimos_turnos_pendientes = turnos_pendientes_ordenados[:5]
        return ultimos_turnos_pendientes