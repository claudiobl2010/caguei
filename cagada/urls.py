from django.conf.urls.defaults import patterns

urlpatterns = patterns('caguei.cagada.views',

    (r'^$', 'home'),
    (r'^cagar$', 'cagar'),
    (r'^url/(?P<url_id>\d+)/detalhe/?$', 'url_detalhe'),

)
