from django.views import View
from .models import User
from django.http import JsonResponse
from django.forms.models import model_to_dict

class ExistenciaUsuario(View):
    def get(self, request, pk):
        try:
            usuario = User.objects.get(pk=pk)
        except:
            return JsonResponse(False, safe=False)
        return JsonResponse(True, safe=False)
        