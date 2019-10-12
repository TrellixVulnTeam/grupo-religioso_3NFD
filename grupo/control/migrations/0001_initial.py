# Generated by Django 2.2.6 on 2019-10-06 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comunidad', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('comunidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.Comunidad')),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_actividad', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('lugar', models.CharField(max_length=200)),
                ('participantes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.Persona')),
            ],
        ),
    ]
