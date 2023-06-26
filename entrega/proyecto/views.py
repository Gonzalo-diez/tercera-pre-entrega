from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import Publicacion, Comentario
from .forms import FormularioRegistroUsuario, FormularioNuevoProducto, FormularioComentario
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth import login

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'proyecto/inicio.html'

class ConsolaPage(LoginRequiredMixin, ListView):
    context_object_name = 'consolas'
    template_name = 'proyecto/listaConsola.html'
    login_url = '/login/'

    def get_queryset(self):
        return Publicacion.objects.filter(producto='consola')


class CelularPage(LoginRequiredMixin, ListView):
    context_object_name = 'celulares'
    template_name = 'proyecto/listaCelular.html'
    login_url = '/login/'

    def get_queryset(self):
        return Publicacion.objects.filter(producto='celular')

class ComputadoraPage(LoginRequiredMixin, ListView):
    context_object_name = 'computadoras'
    template_name = 'proyecto/listaComputadora.html'
    login_url = '/login/'

    def get_queryset(self):
        return Publicacion.objects.filter(producto='computadora')


class ConsolaDetalle(LoginRequiredMixin, DetailView):
    model = Publicacion
    context_object_name = 'consola'
    template_name = 'proyecto/detalleConsola.html'

class CelularDetalle(LoginRequiredMixin, DetailView):
    model = Publicacion
    context_object_name = 'celular'
    template_name = 'proyecto/detalleCelular.html'

class ComputadoraDetalle(LoginRequiredMixin, DetailView):
    model = Publicacion
    context_object_name = 'computadora'
    template_name = 'proyecto/detalleComputadora.html'

class Registro(FormView):
    template_name = 'proyecto/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Inicio')
        return super(Registro, self).get(*args, **kwargs)

class LoginPage(LoginView):
    template_name = 'proyecto/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('Inicio')

    def get_success_url(self):
        return reverse_lazy('Inicio')

class AgregarPublicacion(LoginRequiredMixin, View):
    form_class = FormularioNuevoProducto
    template_name = 'proyecto/agregarPublicacion.html'
    success_url = reverse_lazy('Inicio')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect(self.success_url)
        else:
            print(form.errors)
        return render(request, self.template_name, {'form': form})


class ComentarioPage(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'proyecto/comentario.html'
    success_url = reverse_lazy('Inicio')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPage, self).form_valid(form)
