# Generated by Django 4.2.17 on 2024-12-19 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
        ('foto', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='bio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bio.bio'),
        ),
        migrations.AddField(
            model_name='persona',
            name='fotoPerf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foto.foto'),
        ),
    ]