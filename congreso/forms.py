from django.forms import ModelForm
from django.contrib.admin import widgets  
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import *
from congreso.models import *
from congreso.timeselectwidget import SelectTimeWidget
from congreso.paises import PAISES
from congreso.tipos import TIPOS
from django.contrib.formtools.wizard.views import SessionWizardView


class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = ('Nombre','Pagina','Tipo','Costo','Descripcion','Fecha_I','Hora_I','Fecha_F','Hora_F','Pais','Estado','Municipio','Direccion','Referencias','Director','Correo')
		widgets = {
		'Nombre':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Pagina':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Tipo':Select(choices = TIPOS),
		'Costo':TextInput(attrs={'maxlength': 250, 'size':10}),
		'Descripcion': Textarea(attrs={'cols': 54, 'rows': 5}),
		'Pais':Select(choices=PAISES),
		'Estado':TextInput(attrs={'maxlength': 250, 'size':75}),
		#'Estado':Select(choices=ESTADOS),
		'Municipio':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Direccion': Textarea(attrs={'cols': 54, 'rows': 5}),
		'Referencias': Textarea(attrs={'cols': 54, 'rows': 5}),
		'Director':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Correo':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Fecha_I': SelectDateWidget(),
		'Hora_I': SelectTimeWidget(),
		#'Hora_I':SplitHiddenDateTimeWidget(),
		'Fecha_F': SelectDateWidget(),
		'Hora_F': SelectTimeWidget(),
		#'Hora_F':SplitHiddenDateTimeWidget(),
		}
		
		
class FechasClaveForm(ModelForm):
	class Meta:
		model = FechasClave
		fields = ('Fecha','Descripcion')
		widgets = {
			'Fecha':SelectDateWidget(),
			'Descripcion': Textarea(attrs={'cols': 54, 'rows': 5}),
		}
