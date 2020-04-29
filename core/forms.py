from django import forms

from .models import UnidadeOrganizacional, Modalidade, TipoModalidade


class UnidadeOrganizacionalModelForm(forms.ModelForm):

    class Meta:
        model = UnidadeOrganizacional
        fields = ('nome',)


class RelatorioInscricoesForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects)
    modalidade = forms.ModelChoiceField(Modalidade.objects)


class RelatorioAtletasCampusForm(forms.Form):
    unidade_organizacional = forms.ModelChoiceField(UnidadeOrganizacional.objects, required=False)

class RelatorioAtletasModalidadeForm(forms.Form):
    modalidade = forms.ModelChoiceField(Modalidade.objects, required=False)


class RelatorioAtletasTipoModalidadeForm(forms.Form):
    tipo_modalidade = forms.ModelChoiceField(TipoModalidade.objects, required=False)
