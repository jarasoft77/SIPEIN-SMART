import django_filters
from django_filters import DateFilter

from .models import *

class DesembarcoFiltro(django_filters.FilterSet):
    #inicio_fecha = DateFilter(field_name='fecha_zarpe_primer', lookup_expr='gte')
    #final_fecha = DateFilter(field_name='fecha_zarpe_primer', lookup_expr='lte')
    
    #fecha_zarpe_primer = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'class': 'datepicker col form-control form-control-sm', 'placeholder': 'DD-MM-YYYY'}))
    fechazarpe_year = django_filters.NumberFilter(field_name='fecha_zarpe_primer', lookup_expr='year')
    fechazarpe_month = django_filters.NumberFilter(field_name='fecha_zarpe_primer', lookup_expr='month')
    
    class Meta:
        model = Desembarco
        fields = {
            'registro': ['exact'],
            'fecha_zarpe_primer': ['exact'],
            'pesqueria_id': ['exact'],
            'embarcacion': ['exact'],
            'capitan': ['exact'],
            'registrador': ['exact']
        }
        
        
class EspecieFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Especie
        fields = {
            'nombre_vulgar': ['icontains'],
            'nombre_taxa': ['icontains'],
            'grupo_id': ['exact'], 
            'familia': ['exact']
        }


class SitioFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Sitio_Desembarco
        fields = {
            'nombre': ['icontains']
        }        


class FamiliaFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Familia
        fields = {
            'nombre': ['icontains']
        }                


class CategoriaFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Categoria
        fields = {
            'nombre': ['icontains']
        }    


class EstadoFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Estado
        fields = {
            'nombre': ['icontains']
        }            


class CaladeroFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Caladero
        fields = {
            'nombre': ['icontains']
        }            


class EmbarcacionFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Embarcacion
        fields = {
            'nombre': ['icontains']
        }   


class CostoFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Costo
        fields = {
            'nombre': ['icontains']
        }   


class CapitanFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Capitan
        fields = {
            'nombre': ['icontains']
        }   


class RegistradorFiltro(django_filters.FilterSet):
    
    class Meta:
        model = Registrador
        fields = {
            'nombre': ['icontains']
        }           