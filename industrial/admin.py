from django.contrib import admin
from .models import Sitio_Desembarco, Control_Actividad, Desembarco, Especie, Captura_Esfuerzo_Abordo, Embarcacion
# Register your models here.

admin.site.register(Sitio_Desembarco)
admin.site.register(Control_Actividad)
admin.site.register(Desembarco)
admin.site.register(Especie)
admin.site.register(Captura_Esfuerzo_Abordo)
admin.site.register(Embarcacion)