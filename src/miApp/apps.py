from django.apps import AppConfig

#Importando los manejadores
from miApp.headlers import imagen_guardada_callback, imagen_borrada_callback

#Importando las señales
from django.db.models.signals import post_save
from django.db.models.signals import post_delete


class MiappConfig( AppConfig ):
	name = 'miApp'

	def ready( self ):
		from miApp.models import Imagen

		post_save.connect( imagen_guardada_callback, sender = Imagen )
		post_delete.connect( imagen_borrada_callback, sender = Imagen )