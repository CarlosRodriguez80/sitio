from django.contrib import admin

# Register your models here.
from .models import Profesor
from .models import Universidad
from .models import Unidad,User
from .models import Config_pagina
from django.core.mail import send_mail

class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'provincia','logo')
    search_fields = ['nombre', 'ciudad', 'provincia']

class UnidadAdmin(admin.ModelAdmin):
    list_display = ('nombre','universidad')
    search_fields = ['nombre']

class ProfesorAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('nombre', 'apellido', 'apodo')
        }),
        ('Detalle', {
            'classes': ('collapse',),
            'fields': ('foto', 'linkedin', 'confirmado_flag', 'universidad', 'unidad','user')
        }),
    )

    def save_model(self,request,obj,form,change):
        user_id = int(request.POST['user'])
        user = User.objects.get(id=user_id)
        flag = request.POST['confirmado_flag']
        if flag == '1':
            send_mail('Recomendacion de Profesor', 'Su recomendacion fue acptada, ya puede calificar', 'carlosrodriguez.upe@gmail.com', [user.email])
            super(Profesor, obj).save()
        elif flag == '2':
            super(Profesor, obj).save()
        else:   
            super(Profesor, obj).delete()
            send_mail('Recomendacion de Profesor', 'Su recomendacion sue rechazada', 'carlosrodriguez.upe@gmail.com', ['carlosrodriguez.upe@gmail.com'])
        #super(Profesor, obj).save()

class Config_paginaAdmin(admin.ModelAdmin):
    list_display = ('paginacion', 'top', 'recientes', 'populares')

admin.site.register(Universidad, UniversidadAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Config_pagina, Config_paginaAdmin)