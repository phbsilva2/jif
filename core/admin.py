from django.contrib import admin

from .models import UnidadeOrganizacional


@admin.register(UnidadeOrganizacional)
class UnidadeOrganizacionalAdmin(admin.ModelAdmin):
    list_filter = ('nome',)

