from django.db import models

class UnidadeOrganizacional(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Unidade Organizacional'
        verbose_name_plural = 'Unidades Organizacionais'

    def __str__(self):
        return self.nome

