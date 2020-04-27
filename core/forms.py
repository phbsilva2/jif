from django import forms

from .models import UnidadeOrganizacional, Modalidade


class UnidadeOrganizacionalModelForm(forms.ModelForm):

    class Meta:
        model = UnidadeOrganizacional
        fields = ('nome',)


class InscricoesRelatorioForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects)
    modalidade = forms.ModelChoiceField(Modalidade.objects)
