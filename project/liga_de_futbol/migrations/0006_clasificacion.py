# Generated by Django 5.1.1 on 2024-09-15 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga_de_futbol', '0005_alter_equipo_puntos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='liga_de_futbol.equipo')),
            ],
        ),
    ]
