from django.db import models
from django.contrib.auth.models import User

ZONAS_PESCA = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
]

BANDERA_CALIDAD = [
    (1, 'NO EVALUADO'),
    (2, 'VALIDADO'),
    (3, 'MALO')
]

TIPO_CAPTURA = [
    ('CO', 'CAPTURA OBJETIVO'),
    ('CI', 'CAPTURA INCIDENTAL'),
    ('D', 'DESCARTE')
]

REGION_COSTA = [
    (1, 'CARIBE'),
    (2, 'PACIFICO')
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

TIPO_PESQUERIA = [
    (1, 'CAS'),
    (2, 'CAP')
]

class Sitio_Desembarco(models.Model):
    nombre = models.TextField(max_length=50, verbose_name='Nombre', unique=True)
    coord_lon = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Longitud')
    coord_lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Latitud')
    costa_id = models.PositiveSmallIntegerField(choices=REGION_COSTA, null=True)

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']
    
class Embarcacion(models.Model):
    nombre = models.TextField(max_length=100, unique=True, verbose_name='Nombre')
    tamano_red = models.DecimalField(blank=True, max_digits=5, decimal_places=2, null=True, verbose_name='Tamaño de red')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']


class Familia(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.title()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']


class Especie(models.Model):
    nombre_vulgar = models.CharField(max_length=100, verbose_name='Nombre vulgar')
    nombre_taxa = models.CharField(max_length=100, unique=True, verbose_name='Taxa')
    grupo_id = models.PositiveSmallIntegerField(choices=GRUPO_ESPECIE, verbose_name='Grupo de Especie')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, verbose_name='Familia')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True, blank=True)

    def nombre_especie(self):
        return "{} - ({})".format(self.nombre_vulgar, self.nombre_taxa)
    
    def __str__(self):
        return self.nombre_especie()
    
    def save(self, *args, **kwargs):
        self.nombre_vulgar = self.nombre_vulgar.upper()
        self.nombre_taxa = self.nombre_taxa.title()
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        if self.imagen.name:
            self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        ordering = ['nombre_vulgar']


class Categoria(models.Model):
    nombre = models.TextField(max_length=100, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']


class Estado(models.Model):
    nombre = models.TextField(max_length=100, unique=True, verbose_name='Nombre')
    factor_conversion = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, verbose_name='Factor de Conversión')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']


class Caladero(models.Model):
    nombre = models.TextField(max_length=50, verbose_name='Nombre', unique=True)
    coord_lon = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Longitud')
    coord_lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Latitud')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)    

class Registrador(models.Model):
    nombre = models.TextField(max_length=100, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']


class Capitan(models.Model):
    nombre = models.TextField(max_length=100, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']

class Costo(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre')

    def __str__(self):
        return self.nombre 
    
    def save(self, *args, **kwargs):
        self.nombre = self.nombre.upper()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['nombre']


class Control_Actividad(models.Model):
    monitoreada = models.BooleanField(default=False)
    registro = models.PositiveSmallIntegerField(blank=True)
    pesqueria_id = models.PositiveSmallIntegerField(choices=TIPO_PESQUERIA)
    sitio = models.ForeignKey(Sitio_Desembarco, on_delete=models.CASCADE)
    embarcacion = models.ForeignKey(Embarcacion, on_delete=models.CASCADE)
    fecha_zarpe_primer = models.DateField(null=True, blank=True)
    fecha_zarpe_real = models.DateField(null=True, blank=True)
    fecha_arribo = models.DateField(null=True, blank=True)
    fecha_arribo_real = models.DateField(null=True, blank=True)
    dias_no_pesca = models.PositiveSmallIntegerField()
    dias_fuera_puerto = models.PositiveSmallIntegerField()
    validada = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Captura_Esfuerzo_Abordo(models.Model):
    monitoreo = models.PositiveSmallIntegerField(blank=True)
    lance = models.PositiveSmallIntegerField(blank=True)
    fecha_lance = models.DateField(null=True, blank=True)
    pesqueria_id = models.PositiveSmallIntegerField(choices=TIPO_PESQUERIA)
    estado_mar = models.PositiveSmallIntegerField(blank=True)
    sitio = models.ForeignKey(Sitio_Desembarco, on_delete=models.CASCADE)
    registrador = models.ForeignKey(Registrador, on_delete=models.CASCADE)
    caladero = models.ForeignKey(Caladero, on_delete=models.CASCADE)
    embarcacion = models.ForeignKey(Embarcacion, on_delete=models.CASCADE)
    longitud_cable = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    hora_inicial = models.DateTimeField(null=True, blank=True)
    hora_final = models.DateTimeField(null=True, blank=True)
    descarte = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Desembarco(models.Model):
    registro = models.PositiveSmallIntegerField(verbose_name='Registro', null=False, blank=False)
    fecha_zarpe_primer = models.DateField(verbose_name='Fecha del Primer Zarpe', null=False, blank=False)
    pesqueria_id = models.PositiveSmallIntegerField(choices=TIPO_PESQUERIA, verbose_name='Tipo de Pesquería', null=False, blank=False)
    sitio = models.ForeignKey(Sitio_Desembarco, on_delete=models.CASCADE, verbose_name='Sitio de Desembarco', null=False, blank=False)
    embarcacion = models.ForeignKey(Embarcacion, on_delete=models.CASCADE, verbose_name='Embarcación', null=False, blank=False)
    capitan = models.ForeignKey(Capitan, on_delete=models.CASCADE, verbose_name='Capitán', null=False, blank=False)
    zonas_pesca = models.CharField(max_length=1, choices=ZONAS_PESCA, verbose_name='Zonas de pesca', null=True, blank=True)
    lance_dia = models.PositiveSmallIntegerField(verbose_name='Número de Lances por día', null=False, blank=False)
    pescadores = models.PositiveSmallIntegerField(verbose_name='Número de Pescadores', null=False, blank=False)
    registrador = models.ForeignKey(Registrador, on_delete=models.CASCADE, verbose_name='Registrador de Campo', null=False, blank=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    bandera = models.PositiveSmallIntegerField(choices=BANDERA_CALIDAD, verbose_name='Bandera', null=False, blank=False, default=1)

class Desembarco_Capturas(models.Model):
    desembarco = models.ForeignKey(Desembarco, on_delete=models.CASCADE)
    tipo_captura = models.CharField(max_length=2, choices=TIPO_CAPTURA, verbose_name='Tipo de Captura', null=False, blank=False)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False, blank=False)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Peso (kg)')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Precio kilo') 

class Desembarco_Costos(models.Model):
    desembarco = models.ForeignKey(Desembarco, on_delete=models.CASCADE)
    costo = models.ForeignKey(Costo, on_delete=models.CASCADE, null=False, blank=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor ($)')