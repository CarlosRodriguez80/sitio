from django.contrib import admin

# Register your models here.
from .models import Profesor
from .models import Universidad
from .models import Unidad
from .models import Config_pagina

class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'provincia','logo')
    search_fields = ['nombre', 'ciudad', 'provincia']

class UnidadAdmin(admin.ModelAdmin):
    list_display = ('nombre','universidad')
    search_fields = ['nombre']

class ProfesorAdmin(admin.ModelAdmin):
     fieldsets = (
        ('Detalle', {
            'classes': ('collapse',),
            'fields': ('foto', 'linkedin', 'confirmado_flag', 'universidad', 'unidad','user')
        }),
    )

class Config_paginaAdmin(admin.ModelAdmin):
    list_display = ('paginacion', 'top', 'recientes', 'populares')

admin.site.register(Universidad, UniversidadAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Config_pagina, Config_paginaAdmin)