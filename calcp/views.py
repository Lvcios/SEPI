import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from datetime import date, datetime, timedelta
import calendar
from cal.models import *
from django.template import RequestContext #necesaria para jalar los estilos css

from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory

mnames = "January February March April May June July August September October November December"
mnames = mnames.split()
#@login_required
def month(request, year, month, change=None):
#def month(request,change=None):
	#year = 2012
	#month = 10
	year, month = int(year), int(month)
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
	# apply next / previous change
	if change in ("next", "prev"):
		now, mdelta = date(year, month, 15), timedelta(days=31)
		if change == "next":   mod = mdelta
		elif change == "prev": mod = -mdelta
		year, month = (now+mod).timetuple()[:2]
	# init variables
	cal = calendar.Calendar()
	month_days = cal.itermonthdays(year, month)
	nyear, nmonth, nday = time.localtime()[:3]
	lst = [[]]
	week = 0

	# make month lists containing list of days for each week
	# each day tuple will contain list of entries and 'current' indicator
	for day in month_days:
		entries = current = False   # are there entries for this day; current day?
		if day:
			entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
			if day == nday and year == nyear and month == nmonth:
				current = True
		lst[week].append((day, entries, current))
		if len(lst[week]) == 7:
			lst.append([])
			week += 1


	#esto debe ir en la plantilla para generar un link al evento sobre el dia {% url cal.views.day year month day %}
	#return render_to_response("mes.html", {"year":year, "month":month,"month_days":lst, "mname":mnames[month-1]})
	return render_to_response("mes.html", {"year":year, "month":month,"month_days":lst, "mname":mnames[month-1],"year_prev":year_prev,"year_next":year_next,"month_prev":month_prev,"month_next":month_next},RequestContext(request))
	
	
	#VISTA DEL DIA
def day(request, year, month, day):
	#"""Entries for the day."""
	EntriesFormset = modelformset_factory(Entry, extra=1, exclude=("creator", "date"),can_delete=True)
	
	if request.method == 'POST':
		formset = EntriesFormset(request.POST)
		if formset.is_valid():
			# add current user and date to each entry & save
			entries = formset.save(commit=False)
			for entry in entries:
				entry.creator = request.user
				entry.date = date(int(year), int(month), int(day))
				entry.save()
			return HttpResponseRedirect(reverse("dbe.cal.views.month", args=(year, month)))
	else:
		# display formset for existing enties and one extra form
		formset = EntriesFormset(queryset=Entry.objects.filter(date__year=year,date__month=month, date__day=day, creator=request.user))
	return render_to_response("day.html", add_csrf(request, entries=formset, year=year,month=month, day=day),RequestContext(request))
	
def add_csrf(request, ** kwargs):
	#"""Add CSRF and user to dictionary."""
	d = dict(user=request.user, ** kwargs)
	d.update(csrf(request))
	return d
	
	