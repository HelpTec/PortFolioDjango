# Generated by Django 4.2.17 on 2025-02-09 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_remove_persona_bio_remove_persona_fotoperf_and_more'),
        ('bio', '0006_remove_bio_textos_bio_textos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='textos',
        ),
        migrations.AlterField(
            model_name='bio',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bio', to='persona.persona'),
        ),
    ]
