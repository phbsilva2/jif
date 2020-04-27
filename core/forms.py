from django import forms

from .models import UnidadeOrganizacional


class UnidadeOrganizacionalModelForm(forms.ModelForm):

    class Meta:
        model = UnidadeOrganizacional
        fields = ('nome',)
