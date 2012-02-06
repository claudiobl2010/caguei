from django.db import models

class Url(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    descricao = models.CharField(max_length=500, null=False)
    url = models.CharField(max_length=1000, null=False)
    qtd = models.IntegerField(null=False, default=0)
    ranking = models.IntegerField(null=False, default=0)
    hash = models.CharField(max_length=100, null=False)
    criacao = models.DateTimeField(null=False, auto_now_add=True)

class Assunto(models.Model):
    descricao = models.CharField(max_length=1000, null=False)
    qtd = models.IntegerField(null=False, default=0)
    ranking = models.IntegerField(null=False, default=0)
    hash = models.CharField(max_length=100, null=False)
    criacao = models.DateTimeField(null=False, auto_now_add=True)

class Log(models.Model):
    cagada_id = models.IntegerField(null=False)
    tipo = models.CharField(max_length=1, null=False, choices=(('U', 'Url'), ('A', 'Assunto')))
    ip = models.CharField(max_length=15, null=False)
    data = models.DateTimeField(null=False, auto_now_add=True)
