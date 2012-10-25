from django.forms import ModelForm
from django import forms
from docgenerator.models import *

class OficioForm(ModelForm):
	class Meta:
		model = Oficio
		
class DestinoForm(ModelForm):
	class Meta:
		model = Destino
		
class OfiDestForm(ModelForm):
	class Meta:
		model =OfiDest
		
class OfiCCForm(ModelForm):
	class Meta:
		model = OfiCC
		
class ContactForm1(forms.Form):
	subject = forms.CharField(max_length=100)
	sender = forms.EmailField()
	
class ContactForm2(forms.Form):
	message = forms.CharField(widget = forms.Textarea)