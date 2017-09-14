from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from miApp.settings_miApp import DIMENSIONES

import os

# Create your views here.

def home( request ):
	"""
		Vista principal de la aplicación
	"""

	lista_url = []

	#Obtiendo la lista de directorios creados dentro de mis_imagenes
	ruta = os.path.join( settings.MEDIA_ROOT, 'mis_imagenes' )
	lista_dir = os.listdir( ruta )

	# Recorre la cantidad de directorios creados al subir las imágenes
	for directorio in lista_dir:

		fs = FileSystemStorage( 
			location=os.path.join( ruta, directorio ), 
			base_url='/media/mis_imagenes/' + directorio + '/' 
		)

		url = []

		lista_img = os.listdir( os.path.join( ruta, directorio ) )

		#Recorre las imágenes que se encuentran dentro de los directorios creados
		for i in range( len( lista_img ) ):

			url_img 	= fs.url( lista_img[i] )
			dimen 		= DIMENSIONES[i]

			url.append( { 'url_img':url_img, 'dimension':str( dimen ) } )

		lista_url.append( url )

	#Creando el contexto
	mi_contexto = {
		'lista_url' : lista_url
	}

	return render( request, template_name = 'index.html', context=mi_contexto )