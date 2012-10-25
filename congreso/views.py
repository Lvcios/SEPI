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

def nuevo_evento(request):
	if request.method == 'POST':
		formulario = EventoForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save(commit = True)
			return HttpResponseRedirect('/')
			#return render_to_response('destino.html',{'formulario':formulario},context_instance = RequestContext(request))
	else:
		formulario = EventoForm()
	return render_to_response('evento.html',{'formulario':formulario},context_instance = RequestContext(request))# Create your views here.



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
	eventos = Evento.objects.filter(Fecha_I__year=year, Fecha_I__month=month, Fecha_I__day=day, Validado = True)
	return render_to_response("dia.html",{"eventos":eventos,"Fecha_D":day,"Fecha_M":mnames[month-1],"Fecha_A":year},RequestContext(request))
	
	

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
	
