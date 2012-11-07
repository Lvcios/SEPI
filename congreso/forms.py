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
		'Costo':TextInput(attrs={'maxlength': 250, 'size':10}),
		'Descripcion': Textarea(attrs={'cols': 54, 'rows': 5}),
		'Pais':Select(choices=PAISES),
		'Estado':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Municipio':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Direccion': Textarea(attrs={'cols': 54, 'rows': 5}),
		'Referencias': Textarea(attrs={'cols': 54, 'rows': 5}),
		'Director':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Correo':TextInput(attrs={'maxlength': 250, 'size':75}),
		'Fecha_I': SelectDateWidget(),
		'Hora_I': SelectTimeWidget(),
		'Fecha_F': SelectDateWidget(),
		'Hora_F': SelectTimeWidget(),
		}
		
		
class FechasClaveForm(ModelForm):
	class Meta:
		model = FechasClave
		fields = ('Fecha_A','Descripcion_A',
				  'Fecha_B','Descripcion_B',
				  'Fecha_C','Descripcion_C',
				  'Fecha_D','Descripcion_D',
				  'Fecha_E','Descripcion_E',
				  'Fecha_F','Descripcion_F',
				  'Fecha_G','Descripcion_G',
				  'Fecha_H','Descripcion_H',
				  'Fecha_I','Descripcion_I',
				  'Fecha_J','Descripcion_J',)
		widgets = {
			'Fecha_A':SelectDateWidget(),
			'Descripcion_A': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_B':SelectDateWidget(),
			'Descripcion_B': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_C':SelectDateWidget(),
			'Descripcion_C': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_D':SelectDateWidget(),
			'Descripcion_D': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_E':SelectDateWidget(),
			'Descripcion_E': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_F':SelectDateWidget(),
			'Descripcion_F': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_G':SelectDateWidget(),
			'Descripcion_G': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_H':SelectDateWidget(),
			'Descripcion_H': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_I':SelectDateWidget(),
			'Descripcion_I': Textarea(attrs={'cols': 54, 'rows': 5}),
			'Fecha_J':SelectDateWidget(),
			'Descripcion_J': Textarea(attrs={'cols': 54, 'rows': 5}),
		}
