# Generated by Django 4.0.4 on 2022-05-07 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turno',
            name='usuario_staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_staff', to=settings.AUTH_USER_MODEL),
        ),
    ]
