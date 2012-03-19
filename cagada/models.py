from django.db import models

class Url(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    descricao = models.CharField(max_length=500, null=False)
    url = models.CharField(max_length=1000, null=False)
    qtd = models.IntegerField(null=False, default=0)
    ranking = models.IntegerField(null=False, default=0)
    hash = models.CharField(max_length=100, null=False)
    criacao = models.DateTimeField(null=False, auto_now_add=True)
    
    def get_titulo_curto(self):
        if len(self.titulo) > 50:
            return '%s ...' % self.titulo[:50]
        else:
            return self.titulo

    def get_url_curta(self):
        if len(self.url) > 50:
            return '%s ...' % self.url[:50]
        else:
            return self.url

class Assunto(models.Model):
    descricao = models.CharField(max_length=1000, null=False)
    qtd = models.IntegerField(null=False, default=0)
    ranking = models.IntegerField(null=False, default=0)
    hash = models.CharField(max_length=100, null=False)
    criacao = models.DateTimeField(null=False, auto_now_add=True)
    
    def get_descricao_curta(self):
        if len(self.descricao) > 50:
            return '%s ...' % self.descricao[:50]
        else:
            return self.descricao

class Log(models.Model):
    cagada_id = models.IntegerField(null=False)
    tipo = models.CharField(max_length=1, null=False, choices=(('U', 'Url'), ('A', 'Assunto'), ('E', 'Erro')))
    ip = models.CharField(max_length=15, null=False)
    data = models.DateTimeField(null=False, auto_now_add=True)
