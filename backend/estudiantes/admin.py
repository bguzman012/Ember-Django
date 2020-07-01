
# Register your models here.
from __future__ import unicode_literals

from django.contrib import admin

from estudiantes import models

admin.site.register(models.Estudiante)  

admin.site.register(models.Representante)