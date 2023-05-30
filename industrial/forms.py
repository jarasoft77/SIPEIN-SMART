from django import forms
from .models import Sitio_Desembarco, Especie, Familia, Caladero, Embarcacion, Capitan, Registrador, Desembarco, Desembarco_Capturas, Categoria, Estado, Costo, Desembarco_Costos
from django.forms import inlineformset_factory


TIPO_PESQUERIA = [
    (1, 'CAS'),
    (2, 'CAP')
]

GRUPO_ESPECIE = [
    (1, 'CRUSTÁCEOS'),
    (2, 'EQUINODERMOS'),
    (3, 'MOLUSCOS'),
    (4, 'PECES'),
    (5, 'POLIQUETOS'),    
    (6, 'CNIDARIOS'),    
    (7, 'RÉPTILES'),    
]

class FormSitio(forms.ModelForm):
    class Meta:
        model = Sitio_Desembarco
        fields = ['nombre', 'coord_lon', 'coord_lat']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Sitio', 'autofocus': 'True'}),
            'coord_lon': forms.NumberInput(attrs={'class': 'form-control'}),
            'coord_lat': forms.NumberInput(attrs={'class': 'form-control'})
        }

class FormEspecie(forms.ModelForm):
    class Meta:
        model = Especie
        fields = ['nombre_vulgar', 'nombre_taxa', 'grupo_id', 'familia', 'imagen']
        widgets = {
            'nombre_vulgar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Especie', 'autofocus': 'True'}),
            'nombre_taxa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Taxa'}),
            'grupo_id': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'familia': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }  

class FormFamilia(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Familia', 'autofocus': 'True'})
        }        

class FormCaladero(forms.ModelForm):
    class Meta:
        model = Caladero
        fields = ['nombre','coord_lon', 'coord_lat']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Caladero', 'autofocus': 'True'}),
            'coord_lon': forms.NumberInput(attrs={'class': 'form-control'}),
            'coord_lat': forms.NumberInput(attrs={'class': 'form-control'}),
        }        

class FormEmbarcacion(forms.ModelForm):
    class Meta:
        model = Embarcacion
        fields = ['nombre','tamano_red']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Embarcación', 'autofocus': 'True'}),
            'tamano_red': forms.NumberInput(attrs={'class': 'form-control'}),
        }            

class FormCosto(forms.ModelForm):
    class Meta:
        model = Costo
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Costo', 'autofocus': 'True'}),
        } 

class FormCapitan(forms.ModelForm):
    class Meta:
        model = Capitan
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Capitán', 'autofocus': 'True'}),
        }                    

class FormRegistrador(forms.ModelForm):
    class Meta:
        model = Registrador
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Registrador', 'autofocus': 'True'}),
        }                            

class FormDesembarco(forms.ModelForm):
    class Meta:
        model = Desembarco
        fields = ['registro', 'fecha_zarpe_primer', 'pesqueria_id', 'sitio', 'embarcacion', 'capitan','lance_dia', 'pescadores', 'registrador']
        
        widgets = {
            'registro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de registro', 'autofocus': 'True'}),
            'fecha_zarpe_primer': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pesqueria_id': forms.RadioSelect(choices=TIPO_PESQUERIA, attrs={'class': 'form-check form-check-inline', 'type': 'radio'}),
            'sitio': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'embarcacion': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'capitan': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'lance_dia': forms.NumberInput(attrs={'class': 'form-control'}),
            'pescadores': forms.NumberInput(attrs={'class': 'form-control'}),
            'registrador': forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Categoría', 'autofocus': 'True'}),
        }     

class FormEstado(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nombre','factor_conversion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Categoría', 'autofocus': 'True'}),
            'factor_conversion': forms.NumberInput(attrs={'class': 'form-control'}),
        }        

class DesembarcoForm(forms.ModelForm):

    class Meta:
        model = Desembarco
        fields = ['registro', 'fecha_zarpe_primer','pesqueria_id', 'sitio', 'embarcacion', 'capitan', 'zonas_pesca', 'lance_dia', 'pescadores','registrador']
        widgets = {
            'registro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de registro', 'autofocus': 'True'}),
            'fecha_zarpe_primer': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
            'pesqueria_id': forms.RadioSelect(choices=TIPO_PESQUERIA, attrs={'class': 'form-check-inline', 'style':'radio'}),
            'sitio': forms.Select(attrs={'class': 'form-select form-select-md'}),
            'embarcacion': forms.Select(attrs={'class': 'form-select form-select-md'}),
            'capitan': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'zonas_pesca': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'lance_dia': forms.NumberInput(attrs={'class': 'form-control'}),
            'pescadores': forms.NumberInput(attrs={'class': 'form-control'}),
            'registrador': forms.Select(attrs={'class': 'form-select form-select-md'}),
        }

class CapturaForm(forms.ModelForm):

    class Meta:
        model = Desembarco_Capturas
        fields = ['tipo_captura', 'especie', 'categoria', 'estado', 'peso', 'precio']
        widgets = {
            'tipo_captura': forms.Select(attrs={'class': 'form-select form-select-sm', 'autofocus': 'True'}),
            'especie': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'categoria': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'estado': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CostoForm(forms.ModelForm):

    class Meta:
        model = Desembarco_Costos
        fields = ['costo', 'valor']
        widgets = {
            'costo': forms.Select(attrs={'class': 'form-select form-select-sm', 'autofocus': 'True'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        }

CapturaFormSet = inlineformset_factory(
    Desembarco, Desembarco_Capturas, form=CapturaForm,
    extra=1, can_delete=True, 
    can_delete_extra=True
)

CostoFormSet = inlineformset_factory(
    Desembarco, Desembarco_Costos, form=CostoForm,
    extra=1, can_delete=True, 
    can_delete_extra=True
)