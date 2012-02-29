from django.conf.urls.defaults import patterns

urlpatterns = patterns('caguei.cagada.views',

    (r'^$', 'home'),
    (r'^cagar$', 'cagar'),
    (r'^url/(?P<url_id>\d+)/?$', 'url_detalhe'),
    (r'^criar-assunto/?$', 'criar_assunto'),
    (r'^cagar-assunto/?$', 'cagar_assunto'),

)
