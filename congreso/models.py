#endcoding:utf-8
from django.db import models
from django_countries import CountryField
# Create your models here.


class TipoEvento(models.Model):
	Descripcion = models.CharField(max_length = 100, verbose_name="Tipo de evento",)
	def __unicode__(self):
		return self.Descripcion


class Evento(models.Model):
	Nombre = models.CharField(max_length = 250, verbose_name="Nombre Completo",)
	Pagina = models.URLField(max_length = 500, verbose_name="Web")
	#Tipo= models.CharField(max_length = 50, verbose_name="Tipo")
	Tipo = models.ForeignKey(TipoEvento)
	Costo= models.CharField(max_length = 100, verbose_name="Costo")
	Descripcion = models.TextField(max_length = 100, verbose_name="De que trata")
	Fecha_I = models.DateField(auto_now = False,verbose_name="Fecha inicio")
	Hora_I = models.TimeField(auto_now = False,verbose_name="Hora inicio")
	Fecha_F = models.DateField(auto_now = False,verbose_name="Fecha Fin")
	Hora_F = models.TimeField(auto_now = False,verbose_name="Hora fin")
	Pais = CountryField(verbose_name="Pais")
	Estado = models.CharField(max_length = 100, verbose_name="Estado")
	Municipio = models.CharField(max_length = 100, verbose_name="Municipio")
	Direccion = models.TextField(verbose_name="Domicilio")
	Referencias = models.TextField(verbose_name="Referencias",blank = "True")
	Director = models.CharField(max_length = 100, verbose_name="Director del evento")
	Correo = models.EmailField(max_length = 100, verbose_name="E-mail de contacto")
	Validado = models.BooleanField(blank = "True")
	def __unicode__(self):
		return self.Nombre + ' ' + str(self.Fecha_I) + ', Validado :' + str(self.Validado)
	

class FechasClave(models.Model):
	Evento = models.ForeignKey(Evento)
	Fecha_A = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_A = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_B = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_B = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_C = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_C = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_D = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_D = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_E = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_E = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_F = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_F = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_G = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_G = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_H = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_H = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_I = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_I = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	Fecha_J = models.DateField(auto_now = False,verbose_name="Fecha",null = "True",blank = "True")
	Descripcion_J = models.TextField(max_length = 100, verbose_name="Descripcion",blank = "True")
	def __unicode__(self):
		#return self.Evento.Nombre + ' ' + str(self.Fecha) + ', Para:' + str(self.Descripcion)
		#return str(self.Fecha) + ', Para:' + str(self.Descripcion)
		return self.Evento.Nombre + ', Listado de Fechas Importantes'
