from django.views import View
from .models import Turno
from django.http import JsonResponse

class TurnosCreados(View):
    def get(self, request):
        turnos = Turno.objects.all()
        lista_turnos = list(turnos.values())
        return JsonResponse(lista_turnos, safe=False)