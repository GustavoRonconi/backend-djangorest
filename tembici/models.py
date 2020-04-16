from django.db import models


class ClassificacaoViagem(models.Model):
    models.CharField(max_length=100)


class Viagem(models.Model):
    data_inicio = models.DateTimeField(null=False)
    data_fim = models.DateTimeField(null=False)
    classificacao = models.OneToOneField(
        ClassificacaoViagem, primary_key=True, null=False
    )
    nota = models.IntegerField(null=False)
