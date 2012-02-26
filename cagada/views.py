# coding: utf-8
#!/usr/bin/env python

import simplejson
import urllib2
import hashlib

from datetime import datetime, timedelta
from BeautifulSoup import BeautifulSoup

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.db.models import F

from cagada.models import Url, Assunto, Log

def home(request):

    return render_to_response('home.html')

def cagar(request):
    # Hash da URL
    url = request.POST['url']
    hash = hashlib.md5(url.lower()).hexdigest()
    
    # Verifica se usuário já cagou na URL
    cagadas = request.session.get('cagadas').split(',') if request.session.get('cagadas') else []
    if cagadas.count(hash):
        return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'Você já cagou para essa URL.'}), content_type="application/json; charset=UTF-8")
        
    # Verifica se foi atingida a QTD máxima de cagadas por hora (máximo de 100 cagadas)
    data_ultima_hora = datetime.now() - timedelta(hours=1)
    qtd = Log.objects.filter(ip=request.META['REMOTE_ADDR'], data__gt=data_ultima_hora).count()
    if qtd > 100:
        return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'Você atingiu a quantidade máxima de cagadas por hora.'}), content_type="application/json; charset=UTF-8")
        
    # Verifica se a URL já foi cagada alguma vez
    urls = Url.objects.filter(hash=hash)

    if urls:
        # Se a URL já foi cagada alguma vez, basta somar + 1 a sua quantidade
        Url.objects.update(qtd=F('qtd')+1)
        url_obj = urls[0]
    else:
        # Se a URL nunca foi cagada, verifica se a mesma é válida
        try:
            page = urllib2.urlopen(url, timeout=3)
            content = page.read()
        except Exception, e:
            # Se a URL informada for inválida, é necessário logar a ação desse IP, afim de evitar um ataque com URLs inválidas, que será bloqueado com a verificação de QTD máxima de cagadas por hora
            log = Log(cagada_id=0, tipo='E', ip=request.META['REMOTE_ADDR'])
            log.save()
            return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'A URL informada não é válida.'}), content_type="application/json; charset=UTF-8")

        # Faz um parser no documento HTML afim de recuperar o title e o description
        document = BeautifulSoup(content)

        try:
            titulo = document.head.title.string
        except Exception, e:
            titulo = 'Não encontrado'

        try:
            descricao = document.find('meta', {'name':'description'}).get('content')
        except Exception, e:
            descricao = 'Não encontrado'

        url_obj = Url(titulo=titulo, descricao=descricao, url=url, hash=hash, qtd=1)
        url_obj.save()

    # Joga o Hash da URL cagada na Session
    cagadas.append(hash)
    request.session['cagadas'] = ','.join(cagadas)
    
    # Log do IP client que deu a cagada na URL
    log = Log(cagada_id=1, tipo='U', ip=request.META['REMOTE_ADDR'])
    log.save()
    
    return HttpResponse(simplejson.dumps({'tipo':'SUCCESS', 'msg':'Você e + %s pessoas cagaram para isso.' % url_obj.qtd if urls else 'Você acaba de dar uma nova cagada. Parabéns!', 'url': {'id': url_obj.id, 'qtd': url_obj.qtd}}), content_type="application/json; charset=UTF-8")

def url_detalhe(request, url_id):
    url_obj = get_object_or_404(Url, pk=url_id)

    return render_to_response('url-detalhe.html', {'url':url_obj})
