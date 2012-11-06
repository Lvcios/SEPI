#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from congreso.forms import *
from congreso.views import *
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
	#project's urls
	url(r'^registro/$','congreso.views.nuevo_evento'),
	url(r'^fechas/$','congreso.views.nuevas_fecha'),
	url(r"^$", "congreso.views.vista_mes"),
	url(r"^(\d+)/(\d+)/$", "congreso.views.vista_mes"),
	url(r"^(\d+)/(\d+)/(\d+)/$", "congreso.views.vista_dia"),
	url(r'^formwizard/$', EventoWizard.as_view([EventoForm, FechasClaveForm])),
	url(r'^contact/$', ContactWizard.as_view([EventoForm, FechasClaveForm])),
	#admin's urls
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
)
