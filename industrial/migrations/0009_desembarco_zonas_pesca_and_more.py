# Generated by Django 4.1.3 on 2023-05-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrial', '0008_profile_familymember'),
    ]

    operations = [
        migrations.AddField(
            model_name='desembarco',
            name='zonas_pesca',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True, verbose_name='Zonas de Pesca'),
        ),
        migrations.AlterField(
            model_name='desembarco_capturas',
            name='tipo_captura',
            field=models.CharField(choices=[('CO', 'CAPTURA OBJETIVO'), ('CI', 'CAPTURA INCIDENTAL'), ('D', 'DESCARTE')], max_length=2, verbose_name='Tipo de Captura'),
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
