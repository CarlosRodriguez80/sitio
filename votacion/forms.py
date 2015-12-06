#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from .models import Profesor,Calificacion
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

#class ContactoForm(forms.Form):
#	correo = forms.EmailField(label='Tu correo electrónico')
#	mensaje = forms.CharField(widget=forms.Textarea)

class ProfesorForm(ModelForm):
    class Meta:
        model = Profesor
        fields = ['apellido','nombre','apodo','universidad', 'unidad','foto', 'linkedin']


class CalificacionForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (CalificacionForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['profesor'].queryset = Profesor.objects.filter(confirmado_flag=1)
  

    class Meta:
        model = Calificacion
        fields = ['profesor', 'comentario','puntaje']

 
class LoginForm(AuthenticationForm):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Username")}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Password")}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                classes = self.fields[f_name].widget.attrs.get('class', '')
                classes += ' has-error'
                self.fields[f_name].widget.attrs['class'] = classes


class RegistracionForm(forms.Form):
    first_name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control','placeholder': _("Nombre")}))
    last_name = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Apellido")}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'maxlength': 60, 'class': 'form-control', 'placeholder': _("Email Address")}))
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Username")}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Password")}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Confirm your password")}))

    def __init__(self, *args, **kwargs):
        super(RegistracionForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class', '')
                    classes += ' has-error'
                    self.fields[f_name].widget.attrs['class'] = classes

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("La Cuenta ya existe."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("La password es diferente."))
        return self.cleaned_data


