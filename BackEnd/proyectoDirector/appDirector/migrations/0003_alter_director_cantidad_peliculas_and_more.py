# Generated by Django 4.2.6 on 2023-11-13 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDirector', '0002_rename_cantpelis_director_cantidad_peliculas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='cantidad_peliculas',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='director',
            name='edad',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='director',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('No Aplica', 'Prefiero no decirlo')], max_length=20),
        ),
        migrations.AlterField(
            model_name='director',
            name='premios',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
