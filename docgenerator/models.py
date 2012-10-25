from django.db import models

# Create your models here.
class Destino(models.Model):
	dest_grado = models.CharField(max_length = 30, verbose_name="Grado:")
	dest_nombre = models.CharField(max_length = 100,verbose_name="Nombre completo:")
	dest_cargo = models.CharField(max_length = 100,verbose_name="Cargo")
	def __unicode__(self):
		return self.dest_grado + ' ' + self.dest_nombre + ' ' + self.dest_cargo

class Oficio(models.Model):
	ofi_num = models.CharField(max_length = 50,verbose_name="Clave:")
	ofi_fecha = models.DateField(auto_now = False,verbose_name="Fecha:")
	ofi_mensaje = models.TextField(verbose_name="Mensaje:")
	dest_nombre = models.ForeignKey(Destino,verbose_name="Remitente:")
	def __unicode__(self):
		return 'Num de Oficio: ' + self.ofi_num + ' ,Fecha: ' + unicode(self.ofi_fecha)

class OfiDest(models.Model):
	ofi_num = models.ForeignKey(Oficio,verbose_name="Clave del oficio:")
	#dest_nombre = models.ForeignKey(Destino,verbose_name="Destino:")
	dest_nombre = models.ManyToManyField(Destino,verbose_name="Destinos:")
	def __unicode__(self):
		return 'Num de Oficio: ' + unicode(self.ofi_num) + ', Dirigido a:' + unicode(self.dest_nombre)

class OfiCC(models.Model):
	ofi_num = models.ForeignKey(Oficio,verbose_name="Clave del oficio:")
	#dest_nombre = models.ForeignKey(Destino,verbose_name="Con copia para:")
	dest_nombre = models.ManyToManyField(Destino,verbose_name="Con copias para:")
	def __unicode__(self):
		return 'Num de Oficio: ' + unicode(self.ofi_num) + ', Con copia para:' + unicode(self.dest_nombre)


	