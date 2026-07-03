from django.contrib import admin
from .models import Autor, Editora, Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'data_nascimento')
    search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'site')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'ano_publicacao', 'preco')
    search_fields = ('titulo',)
    list_filter = ('ano_publicacao',)
    ordering = ('titulo',)