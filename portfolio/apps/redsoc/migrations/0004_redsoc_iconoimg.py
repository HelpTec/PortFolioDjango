# Generated by Django 4.2.17 on 2025-02-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsoc', '0003_alter_redsoc_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='redsoc',
            name='iconoImg',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
