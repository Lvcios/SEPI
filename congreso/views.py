#endcoding:utf-8
from congreso.models import *
from congreso.forms import *
from django.contrib.auth.models import User
import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from datetime import date, datetime, timedelta
import calendar
from django.template import RequestContext #necesaria para jalar los estilos css
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django_countries import CountryField


#FORMS = [("evento",EventoForm),("fechas",FechasClaveForm)]
#TEMPLATES = {"evento":"evento.html","fechas":"fechasclave.html"}


class EventoWizard(SessionWizardView):
	template_name = "form.html"
	#def get_template_names(self):
	#	return [TEMPLATES[self.steps.current]]
		
	def done(self, form_list, **kwargs):
		if form_list[0].is_valid():
			evento = Evento( Referencias = form_list[0].cleaned_data.values()[0],
							Correo = form_list[0].cleaned_data.values()[1],
							Tipo = form_list[0].cleaned_data.values()[2],
							Costo = form_list[0].cleaned_data.values()[3],
							Director = form_list[0].cleaned_data.values()[4],
							Fecha_I = form_list[0].cleaned_data.values()[5],
							Pagina = form_list[0].cleaned_data.values()[6],
							Hora_I = form_list[0].cleaned_data.values()[7],
							Fecha_F =form_list[0].cleaned_data.values()[8],
							Descripcion = form_list[0].cleaned_data.values()[9],
							Nombre = form_list[0].cleaned_data.values()[10],
							Hora_F = form_list[0].cleaned_data.values()[11],
							Direccion = form_list[0].cleaned_data.values()[12],
							Estado = form_list[0].cleaned_data.values()[13],
							#Pais = CountryField(name = str(form_list[0].cleaned_data.values()[14])),
							Pais = form_list[0].cleaned_data.values()[14],
							Municipio = form_list[0].cleaned_data.values()[15],
			)
			evento.save()
			
		if form_list[1].is_valid():
			fechas = FechasClave(Evento = evento,
								Fecha_J = form_list[1].cleaned_data.values()[0],
								Descripcion_I = form_list[1].cleaned_data.values()[1],
								Descripcion_H = form_list[1].cleaned_data.values()[2],
								Fecha_H = form_list[1].cleaned_data.values()[3],
								Fecha_A = form_list[1].cleaned_data.values()[4],
								Fecha_I = form_list[1].cleaned_data.values()[5],
								Fecha_C = form_list[1].cleaned_data.values()[6],
								Fecha_B = form_list[1].cleaned_data.values()[7],
								Fecha_E = form_list[1].cleaned_data.values()[8],
								Fecha_D = form_list[1].cleaned_data.values()[9],
								Fecha_G = form_list[1].cleaned_data.values()[10],
								Fecha_F = form_list[1].cleaned_data.values()[11],
								Descripcion_G = form_list[1].cleaned_data.values()[12],
								Descripcion_F = form_list[1].cleaned_data.values()[13],
								Descripcion_E = form_list[1].cleaned_data.values()[14],
								Descripcion_D = form_list[1].cleaned_data.values()[15],
								Descripcion_C = form_list[1].cleaned_data.values()[16],
								Descripcion_B = form_list[1].cleaned_data.values()[17],
								Descripcion_A = form_list[1].cleaned_data.values()[18],
								Descripcion_J = form_list[1].cleaned_data.values()[19],
			)
			fechas.save()
		
		return HttpResponseRedirect('/')





#LISTA DE MESES
mnames = "Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre"
mnames = mnames.split()



def vista_mes(request, year = None , month = None):
	
	if year and month: 
		year, month = int(year), int(month)
	else:
		year = time.localtime()[0]
		month = time.localtime()[1]
	
	month_prev = month - 1
	month_next = month + 1
	year_prev = year
	year_next = year
	if month_prev == 0:
		year_prev = year - 1
		month_prev = 12
	if month_next == 13:
		year_next = year + 1
		month_next = 1
		
	cal = calendar.Calendar()
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0
	
	for day in month_days:
		eventos = current = False   # are there entries for this day; current day?
		if day:
			eventos = Evento.objects.filter(Fecha_I__year=year, Fecha_I__month=month, Fecha_I__day=day, Validado = True)
			if day == nday and year == nyear and month == nmonth:
				current = True
		lst[week].append((day, eventos, current))
		if len(lst[week]) == 7:
			lst.append([])
			week += 1
	return render_to_response("mes.html", {"year":year, "month":month,"month_days":lst, "mname":mnames[month-1],"mname_next":mnames[month_next-1],"mname_prev":mnames[month_prev-1],
	"year_prev":year_prev,"year_next":year_next,"month_prev":month_prev,"month_next":month_next},RequestContext(request))
	#return render_to_response("index.html", {"year":year, "month":month,"month_days":lst, "mname":mnames[month-1],"year_prev":year_prev,"year_next":year_next,"month_prev":month_prev,"month_next":month_next},RequestContext(request))


def vista_dia(request, year, month, day):
	month = int(month)
	evento = Evento.objects.get(Fecha_I__year=year, Fecha_I__month=month, Fecha_I__day=day, Validado = True)
	fechas = FechasClave.objects.filter(Evento = evento)
	return render_to_response("dia.html",{"evento":evento,"Fecha_D":day,"Fecha_M":mnames[month-1],"Fecha_A":year,"fechas":fechas},RequestContext(request))
	
	

def vista_anual(request, year=None):
	#"""Main listing, years and months; three years per page."""
	# prev / next years
	if year: year = int(year)
	else:    year = time.localtime()[0]
	nowy, nowm = time.localtime()[:2]
	lst = []	

	# create a list of months for each year, indicating ones that contain entries and current
	for y in [year, year + 1]:
		mlst = []
		for n, month in enumerate(mnames):
			evento = current = False   # hay eventos en este mes?
			eventos = Evento.objects.filter(Fecha_I__year=year, Fecha_I__month=n+1, Validado = True)
			if eventos:
				evento = True
			#if y == nowy and n+1 == nowm:
			#	current = True
			mlst.append(dict(n=n+1, name=month, evento=evento, current=current))
		lst.append((y, mlst))
	#return render_to_response("index.html", {"years":lst, "year":year},RequestContext(request))
	return render_to_response("anual.html", {"years":lst, "year":year},RequestContext(request))
	
