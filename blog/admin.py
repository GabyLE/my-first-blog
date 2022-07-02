# Agregar, editar y borrar los post que se han modelado

from django.contrib import admin
from .models import Post

admin.site.register(Post) # hace visible el modelo Post en la página del administrador