from django.db import models

# Create your models here.
class Imagen( models.Model ):

	imagen = models.ImageField( upload_to = 'mis_imagenes' )

	def __str__(self):
		return self.imagen.name

	class Meta:
		db_table 			= 'imagenes'
		verbose_name 		= 'imagen'
		verbose_name_plural = 'imagenes'

		ordering 			= ['id']