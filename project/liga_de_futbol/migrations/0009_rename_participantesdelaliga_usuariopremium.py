# Generated by Django 5.1.1 on 2024-09-19 20:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liga_de_futbol', '0008_rename_usuario_participantesdelaliga'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ParticipantesDeLaLiga',
            new_name='UsuarioPremium',
        ),
    ]
