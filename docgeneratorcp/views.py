# Create your views here.
from docgenerator.models import *
from docgenerator.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.formtools.wizard.views import SessionWizardView


def nuevo_oficio(request):
	if request.method == 'POST':
		formulario = OficioForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/ofidest')
			#return render_to_response('destino.html',{'formulario':formulario},context_instance = RequestContext(request))
	else:
		formulario = OficioForm()
	return render_to_response('oficio.html',{'formulario':formulario},context_instance = RequestContext(request))



def nuevo_ofidest(request):
	if request.method == 'POST':
		formulario = OfiDestForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/oficc')
	else:
		formulario = OfiDestForm()
	return render_to_response('destino.html',{'formulario':formulario},context_instance = RequestContext(request))
	


def nuevo_oficc(request):
	if request.method == 'POST':
		formulario = OfiCCForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/genera')
	else:
		formulario = OfiCCForm()
	return render_to_response('concopia.html',{'formulario':formulario},context_instance = RequestContext(request))
	
def nuevo_docx(request):
	return render_to_response('fin.html',context_instance = RequestContext(request))
	
	
class ContactWizard(SessionWizardView):
	def done(self,form_list,**kwargs):
		return render_to_response('done.html',{'form_data':[form.cleaned_data for form in form_list]})
		

class OficioWizard(SessionWizardView):
	def done(self,form_list,**kwargs):
		return render_to_response('done.html',{'form_data':[form.cleaned_data for form in form_list]})
		
		

