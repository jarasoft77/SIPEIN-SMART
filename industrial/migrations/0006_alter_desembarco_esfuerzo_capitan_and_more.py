# Generated by Django 4.2 on 2023-05-12 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0005_alter_capitan_nombre_alter_registrador_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='capitan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industrial.capitan', verbose_name='Capitán'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='embarcacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industrial.embarcacion', verbose_name='Embarcación'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='fecha_zarpe_primer',
            field=models.DateField(verbose_name='Fecha del Primer Zarpe'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='lance_dia',
            field=models.PositiveSmallIntegerField(verbose_name='Número de Lances por día'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='pescadores',
            field=models.PositiveSmallIntegerField(verbose_name='Número de Pescadores'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='pesqueria_id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'CAS'), (2, 'CAP')], verbose_name='Tipo de Pesquería'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='registrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industrial.registrador', verbose_name='Registrador de Campo'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='registro',
            field=models.PositiveSmallIntegerField(verbose_name='Registro'),
        ),
        migrations.AlterField(
            model_name='desembarco_esfuerzo',
            name='sitio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industrial.sitio_desembarco', verbose_name='Sitio de Desembarco'),
        ),
    ]