#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from docgenerator.views import ContactWizard
from docgenerator.forms import *
from congreso.forms import *
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
	#project's urls
	#url(r'^flat/', include('django.contrib.flatpages.urls')),
	url(r'^oficio/$','docgenerator.views.nuevo_oficio'),
	url(r'^ofidest/$','docgenerator.views.nuevo_ofidest'),
	url(r'^oficc/$','docgenerator.views.nuevo_oficc'),
	url(r'^evento/$','congreso.views.nuevo_evento'),
	#url(r"^calendario/$", "congreso.views.vista_anual"),
	#url(r"^calendario/(\d+)/$", "congreso.views.vista_anual"),
	url(r"^calendario/$", "congreso.views.vista_mes"),
	url(r"^calendario/(\d+)/(\d+)/$", "congreso.views.vista_mes"),
	url(r"^calendario/(\d+)/(\d+)/(\d+)/$", "congreso.views.vista_dia"),
	url(r"^month/(\d+)/(\d+)/$", "cal.views.month"),
	url(r"^month/day/(\d+)/(\d+)/(\d+)/$", "cal.views.day"),
	#url(r"^month/$", "cal.views.month"),
	url(r'^Contacto/$',ContactWizard.as_view([ContactForm1, ContactForm2])),
	url(r'^NuevoOficio/$',ContactWizard.as_view([OficioForm, OfiDestForm, OfiCCForm])),
	#admin's urls
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^', include(admin.site.urls)),
	#(r'^my_admin/jsi18n', 'django.views.i18n.javascript_catalog'),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
