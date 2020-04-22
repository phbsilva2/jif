from django.contrib import admin

from .models import (
    UnidadeOrganizacional,
    TipoModalidade,
    Modalidade,
    Atleta,
)


@admin.register(UnidadeOrganizacional)
class UnidadeOrganizacionalAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10
    actions_on_top = False


@admin.register(TipoModalidade)
class TipoModalidade(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10
    actions_on_top = False


@admin.register(Modalidade)
class Modalidade(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'tipo', 'tipo_modalidade')
    ordering = ('nome',)
    search_fields = ('nome', 'sigla')
    list_per_page = 10
    actions_on_top = False


@admin.register(Atleta)
class Atleta(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'data_nascimento', 'foto')
    ordering = ('nome',)
    search_fields = ('nome', 'matricula')
    list_per_page = 10
    actions_on_top = False
