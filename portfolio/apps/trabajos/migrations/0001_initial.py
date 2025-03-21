# Generated by Django 4.2.17 on 2024-12-19 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
                ('urlEmpresa', models.CharField(max_length=100)),
                ('inicio', models.DateField()),
                ('final', models.DateField(blank=True, null=True)),
                ('avatarImg', models.CharField(max_length=100)),
            ],
        ),
    ]
