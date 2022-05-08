from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm

class UserList(ListView):
    model = User
    template_name='usuarios.html'
    
class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "crear_usuario.html"
    success_url = reverse_lazy('usuarios')
    '''def form_valid(self, form):
        if self.request.user.is_staff:
            return super().form_valid(form)
        return redirect('usuarios')'''

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "crear_usuario.html"
    success_url = reverse_lazy('usuarios')
    '''def form_valid(self, form):
        if self.request.user.is_staff:
            return super().form_valid(form)
        return redirect('usuarios')'''

class UserDeleteView(DeleteView):
    model = User
    template_name = "confirmar_eliminacion_usuario.html"
    success_url = reverse_lazy('usuarios')

class UserAnonymousView(ListView):
    model = User
    template_name='usuarios.html'

    def get_queryset(self):
        usuarios_no_staff = self.model.objects.filter(is_staff=False)
        return usuarios_no_staff