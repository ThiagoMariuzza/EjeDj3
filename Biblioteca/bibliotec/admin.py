from django.contrib import admin
from bibliotec.models import *

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'nombre','numLibros']
    list_display_links = ['nombre', ]
    fieldsets = (
        ('Datos Personales', {
            'fields': ('matricula','tipoPersona','nombre','apellido','numLibros')
        }),
        ('Contacto',{
            'fields': ('correo','telefono')
        }),
    )

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['numEmplado', 'nombre','numLibros']
    list_display_links = ['nombre', ]
    fieldsets = (
        ('Datos Personales', {
            'fields': ('numEmplado','tipoPersona','nombre','apellido','numLibros')
        }),
        ('Contacto',{
            'fields': ('correo','telefono')
        }),
    )

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor','status']
    list_display_links = ['titulo', ]
    fieldsets = (
        ('Libros', {
            'fields': ('autor','titulo','anio','editorial','portada')
        }),
        ('Datos',{
            'fields': ('tipoMaterial','status')
        }),
    )

class RevistaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor','status']
    list_display_links = ['titulo', ]
    fieldsets = (
        ('Libros', {
            'fields': ('autor','titulo','anio')
        }),
        ('Datos',{
            'fields': ('tipoMaterial','status')
        }),
    )


# Register your models here.

admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
admin.site.register(Prestamo)