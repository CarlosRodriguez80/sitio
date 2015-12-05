from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext
from .forms import ProfesorForm,CalificacionForm,RegistracionForm,LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,AnonymousUser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.base import View
from .models import Profesor

# Create your views here.
class IndexView(TemplateView):

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render_to_response('votacion/index_log.html')
        else:
            return render_to_response('votacion/index.html')
    

def nuevo_Recomendado(request):
    if request.method=='POST':
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            profesor = formulario.save(commit=False)
            profesor.user = request.user
            profesor.save()
            return HttpResponseRedirect('/votacion/recomendar')
        #return HttpResponseRedirect(request.user.get_full_name())
    else:
        formulario = ProfesorForm()
        #se usa para filtrar que mostramos formulario.fields["universidad"].queryset = Universidad.objects.filter(nombre='UAI')
        return render_to_response('votacion/recomendarform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nueva_Calificacion(request):
    if request.method=='POST':
        formulario = CalificacionForm(request.POST)
        if formulario.is_valid():
            calificacion = formulario.save(commit=False)
            calificacion.user = request.user
            calificacion.save()
            return HttpResponseRedirect('/votacion/calificar')
    else:
        formulario = CalificacionForm()
        return render_to_response('votacion/calificacionform.html',{'formulario':formulario}, context_instance=RequestContext(request))

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        try:
            return '/votacion'
        except:
            return "/accounts/profile/"


class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/votacion')


class RegistrarView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistracionForm

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/votacion')
        else:
            return super(RegistrarView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = User.objects.create_user(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        return super(RegistrarView, self).form_valid(form)

    def get_success_url(self):
        return '/votacion/registrarme/success/'


class RegistrarSuccessView(TemplateView):
    template_name = 'registration/success.html'


class TopXProfesoresView(generic.ListView):
    model = Profesor
    template_name = "votacion/top.html"
    context_object_name = 'topx_list'
    paginate_by = 1
    #queryset = Pofesor.objects.filter(pub_date__lte=timezone.now(), 
    #                                   is_active=True).order_by('-pub_date')