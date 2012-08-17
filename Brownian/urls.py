from django.conf.urls import patterns, url, include
from dajaxice.core import dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^$', 'Brownian.view.views.query', name='query'),
)

urlpatterns += staticfiles_urlpatterns()