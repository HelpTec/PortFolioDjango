# Generated by Django 4.2.17 on 2025-02-08 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_remove_persona_bio_remove_persona_fotoperf_and_more'),
        ('bio', '0002_remove_bio_texto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='estudios',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='trabajos',
        ),
        migrations.AddField(
            model_name='bio',
            name='fotoPerf',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Bio', to='persona.persona'),
        ),
    ]
