from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from miApp.settings_miApp import DIMENSIONES

import os
import shutil

def imagen_guardada_callback( sender, **kwargs ):
	"""
		Callback llamado cuando se guarda una nueva imagen en la base de datos. Se
		encarga de redimensionar la imagen subida en el panel de 
		administración, a una nueva imagen con dimensiones cuadradas.
	"""

	if kwargs['created']:
		#Si la imagen fue guardada con éxito

		img_db = kwargs['instance']
		imagen = Image.open( settings.MEDIA_ROOT + '/' + img_db.imagen.name )

		#Obteniendo el nombre y el formato de la imagen por separado
		nombre_img, formato_img = img_db.imagen.name.split( '/' )[1].split( '.' )
		
		#creando el directorio que guardará las imágenes redimensionadas
		ruta = os.path.join( os.path.join( settings.MEDIA_ROOT, 'mis_imagenes' ) , nombre_img )		
		os.makedirs( ruta )

		#Redimensionando imágenes
		for dimension in DIMENSIONES:
			imagen_redimensionada = imagen.resize( (dimension, dimension) )
			nombre = nombre_img + '_{}.'.format( dimension ) + formato_img
			imagen_redimensionada.save( ruta + '/' + nombre )

		#Borrando la imagen original
		imagen_origial = nombre_img + '.' + formato_img
		fs = FileSystemStorage( location = os.path.join( settings.MEDIA_ROOT, 'mis_imagenes' ))
		fs.delete( imagen_origial )	

def imagen_borrada_callback( sender, **kwargs ):
	"""
		Callback llamado cuando se borra una 
		imagen de la base de datos
	"""

	nombre_img = kwargs['instance'].imagen.name.split( '/' )[1].split( '.' )[0]

	ruta = os.path.join( os.path.join( settings.MEDIA_ROOT, 'mis_imagenes' ) , nombre_img )
	shutil.rmtree( ruta )