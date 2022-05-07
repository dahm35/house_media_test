from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm

class UserList(ListView):
    model = User
    #context_object_name = ''
    template_name='usuarios.html'

    '''def get_queryset(self):
        return self.model.objects.all()[:2]
        #return super().get_queryset()'''
    
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "crear_usuario.html"
    success_url = reverse_lazy('usuarios')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "crear_usuario.html"
    success_url = reverse_lazy('usuarios')

class UserDeleteView(DeleteView):
    model = User
    template_name = "confirmar_eliminacion_usuario.html"
    success_url = reverse_lazy('usuarios')

class UserAnonymousView(ListView):
    model = User
    #context_object_name = ''
    template_name='usuarios.html'

    def get_queryset(self):
        usuarios_no_staff = self.model.objects.filter(is_staff=False)
        return usuarios_no_staff