# Generated by Django 4.2 on 2023-05-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0003_alter_caladero_coord_lat_alter_caladero_coord_lon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embarcacion',
            name='nombre',
            field=models.TextField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='embarcacion',
            name='tamano_red',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Tamaño de red'),
        ),
    ]
