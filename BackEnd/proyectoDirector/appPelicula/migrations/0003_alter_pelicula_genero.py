# Generated by Django 4.2.6 on 2023-11-16 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPelicula', '0002_rename_clave_foranea_actor_pelicula_actor_protagonista_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(choices=[('Accion', 'Accion'), ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Terror', 'Terror'), ('Otros', 'Otros')], max_length=10),
        ),
    ]
