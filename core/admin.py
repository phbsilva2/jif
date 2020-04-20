from django.contrib import admin

from .models import UnidadeOrganizacional, TipoModalidade


@admin.register(UnidadeOrganizacional)
class UnidadeOrganizacionalAdmin(admin.ModelAdmin):
    ordering = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10
    actions_on_top = False


@admin.register(TipoModalidade)
class TipoModalidade(admin.ModelAdmin):
    ordering = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10
    actions_on_top = False
