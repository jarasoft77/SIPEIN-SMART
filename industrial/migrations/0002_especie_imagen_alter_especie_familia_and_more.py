# Generated by Django 4.2 on 2023-05-10 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='especie',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='familia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industrial.familia', verbose_name='Familia'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='grupo_id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'CRUSTÁCEOS'), (2, 'EQUINODERMOS'), (3, 'MOLUSCOS'), (4, 'PECES'), (5, 'POLIQUETOS'), (6, 'CNIDARIOS'), (7, 'RÉPTILES')], verbose_name='Grupo de Especie'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nombre_taxa',
            field=models.CharField(max_length=100, unique=True, verbose_name='Taxa'),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nombre_vulgar',
            field=models.CharField(max_length=100, verbose_name='Nombre vulgar'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='sitio_desembarco',
            name='coord_lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True, verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='sitio_desembarco',
            name='coord_lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True, verbose_name='Longitud'),
        ),
        migrations.AlterField(
            model_name='sitio_desembarco',
            name='costa_id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'CARIBE'), (2, 'PACIFICO')], null=True),
        ),
        migrations.AlterField(
            model_name='sitio_desembarco',
            name='nombre',
            field=models.TextField(max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]