# coding: utf-8
#!/usr/bin/env python

import simplejson
import urllib2
import hashlib

from BeautifulSoup import BeautifulSoup

from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):

    return render_to_response('home.html')

def cagar(request):
    
    url = request.POST['url']
    
    hash = hashlib.md5(url.lower()).hexdigest()

    try:
        page = urllib2.urlopen(url)
    except Exception, e:
        return HttpResponse(simplejson.dumps({'tipo':'ERROR', 'msg':'URL informada não é uma página válida!!!'}), content_type="application/json; charset=UTF-8")

    content = page.read()
    
    document = BeautifulSoup(content)
    
    titulo = document.head.title.string
    descricao = document.find('meta', {'name':'description'}).get('content')

    return HttpResponse(simplejson.dumps({'tipo': 'SUCCESS', 'msg': 'Ok!!!'}), content_type="application/json; charset=UTF-8")