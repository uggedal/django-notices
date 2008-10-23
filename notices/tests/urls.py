from django.conf.urls.defaults import *

urlpatterns = patterns('notices.tests.views',
    url(r'^redirect_with_success/$', 'redirect_with_success'),
    url(r'^redirect_with_error/$', 'redirect_with_error'),
    url(r'^redirect_with_notice/$', 'redirect_with_notice'),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'template.html'},),
)
