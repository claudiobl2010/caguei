from django.conf.urls.defaults import patterns

urlpatterns = patterns('caguei.cagada.views',

    (r'^$', 'home'),
    (r'^cagar$', 'cagar'),

)
