from django.test import TestCase
from model_mommy import mommy


class UnidadeOrganizacionalTesteCase(TestCase):
    def setUp(self):
        self.unidade_organizacional = mommy.make('UnidadeOrganizacional')

    def test_str(self):
        self.assertEquals(str(self.unidade_organizacional), self.unidade_organizacional.nome)


class TipoModalidadeTestCase(TestCase):
    def setUp(self):
        self.tipo_modalidade = mommy.make('TipoModalidade')

    def test_str(self):
        self.assertEquals(str(self.tipo_modalidade), self.tipo_modalidade.nome)


class ModalidadeTestCase(TestCase):
    def setUp(self):
        self.modalidade = mommy.make('Modalidade')

    def test_str(self):
        self.assertEquals(str(self.modalidade), self.modalidade.nome)


class AtletaTestCase(TestCase):
    def setUp(self):
        self.atleta = mommy.make(('Atleta'))

    def test_str(self):
        self.assertEquals(str(self.atleta), self.atleta.nome)


class AtletaPorModalidade(TestCase):
    def setUp(self):
        self.atleta_por_modalidade = mommy.make('AtletaPorModalidade')

    def test_str(self):
        self.assertEquals(str(self.atleta_por_modalidade),
                          f"{self.atleta_por_modalidade.modalidade}, Lotação Permitida: {self.atleta_por_modalidade.lotacao_permitida}")
