from django.contrib import admin
from .models import Blog, AcercaDe, Entrevista, Post, Analisis


admin.site.register(Entrevista)

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'creado', 'destacado')  # Muestra el campo 'destacado' en el admin
    list_filter = ('creado', 'destacado')  # Permite filtrar por 'destacado'
    search_fields = ('titulo', 'contenido')  # Búsqueda por título y contenido

admin.site.register(Post, PostAdmin)

@admin.register(Analisis)
class AnalisisAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha')  # Campos visibles en la lista del admin
    search_fields = ('titulo', 'categoria')         # Campos de búsqueda
    list_filter = ('categoria', 'fecha')           # Filtros laterales
    ordering = ('-fecha',)                         # Ordenar por fecha descendente

