from django.test import TestCase
from model_mommy import mommy

class UnidadeOrganizacionalTesteCase(TestCase):
    def setUp(self):
        self.unidade_organizacional = mommy.make('UnidadeOrganizacional')

    def test_str(self):
        self.assertAlmostEqual(str(self.unidade_organizacional), self.unidade_organizacional.nome)
