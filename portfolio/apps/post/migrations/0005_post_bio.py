# Generated by Django 4.2.17 on 2025-02-09 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0007_remove_bio_textos_alter_bio_persona'),
        ('post', '0004_remove_post_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='textos', to='bio.bio'),
        ),
    ]
