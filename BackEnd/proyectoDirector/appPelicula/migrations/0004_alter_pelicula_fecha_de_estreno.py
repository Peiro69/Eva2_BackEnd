# Generated by Django 4.2.6 on 2023-11-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPelicula', '0003_alter_pelicula_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='fecha_de_estreno',
            field=models.DateField(default='dd/mm/aaaa'),
        ),
    ]
