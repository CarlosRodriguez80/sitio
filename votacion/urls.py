from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),  name='index'),
    url(r'^recomendar/$', views.nuevo_Recomendado, name='recomendar'),
    url(r'^recomendar/success$', views.recomendarSuccess, name='recomendarSuccess'),
    url(r'^calificar/$', views.nueva_Calificacion, name='calificar'),
    #login
    url(r'^login/$' ,views.LoginView.as_view(),name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	# register
    url(r'^registrarme/$', views.RegistrarView.as_view(), name='registrarme'),
    url(r'^registrarme/success/$',views.RegistrarSuccessView.as_view(), name='registrarme-success'),
    #reportes
    url(r'^recientes/$', views.RecientesProfesoresView, name='recientes'),
    url(r'^populares/$', views.PopularesProfesoresView, name='populares'),
    url(r'^top/$', views.TopXProfesoresView, name='top'),
    url(r'^busca/$', views.BuscarProfesoresView, name='busca'),
]