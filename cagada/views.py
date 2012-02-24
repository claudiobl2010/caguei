# coding: utf-8
#!/usr/bin/env python

import simplejson
import urllib2
import hashlib

from datetime import datetime, timedelta
from BeautifulSoup import BeautifulSoup

from django.shortcuts import render_to_response
from django.http import HttpResponse

from cagada.models import Url, Assunto, Log
from django.db.models import F

def home(request):

    return render_to_response('home.html')

def cagar(request):
    # Hash da URL
    url = request.POST['url']
    hash = hashlib.md5(url.lower()).hexdigest()
    
    # Verifica se usuário já cagou na URL
    cagadas = request.session.get('cagadas').split(',') if request.session.get('cagadas') else []
    if cagadas.count(hash):
        return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'Usuário já cagou para essa URL!!!'}), content_type="application/json; charset=UTF-8")
        
    # Verifica se foi atingida a QTD máxima de cagadas por hora (máximo de 100 cagadas)
    data_ultima_hora = datetime.now() - timedelta(hours=1)
    qtd = Log.objects.filter(ip=request.META['REMOTE_ADDR'], data__gt=data_ultima_hora).count()
    if qtd > 100:
        return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'Usuário atingiu a quantidade máxima de cagadas por hora!!!'}), content_type="application/json; charset=UTF-8")
        
    urls = Url.objects.filter(hash = hash)

    if urls:
        Url.objects.update(qtd = F('qtd') + 1)
    else:
        try:
            page = urllib2.urlopen(url, timeout=3)
        except Exception, e:
            log = Log(cagada_id=0, tipo='E', ip=request.META['REMOTE_ADDR'])
            log.save()
            return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'URL informada não pode ser carregada!!!'}), content_type="application/json; charset=UTF-8")

        content = page.read()
        document = BeautifulSoup(content)

        try:
            titulo = document.head.title.string
        except Exception, e:
            titulo = "Não encontrado"

        try:
            descricao = document.find('meta', {'name':'description'}).get('content')
        except Exception, e:
            descricao = "Não encontrado"

        url_obj = Url(titulo = titulo, descricao = descricao, url = url, qtd = 1, hash = hash)
        url_obj.save()

    # Joga o Hash da URL cagada na Session
    cagadas.append(hash)
    request.session['cagadas'] = ','.join(cagadas)
    
    # Log do IP client que deu a cagada na URL
    log = Log(cagada_id=1, tipo='U', ip=request.META['REMOTE_ADDR'])
    log.save()

    ################################
    # falta tratar o json de sucesso
    # falta tratar as msgs

    return HttpResponse(simplejson.dumps({'tipo': 'SUCCESS', 'msg': 'Ok!!!'}), content_type="application/json; charset=UTF-8")