# Generated by Django 2.1.7 on 2019-05-14 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_termino', models.DateTimeField()),
                ('estatus', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Miembros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.SmallIntegerField()),
                ('tipo_sangre', models.CharField(max_length=4)),
                ('direccion', models.CharField(max_length=200)),
                ('nss', models.CharField(max_length=100)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.Cargo')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.Equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Vueltas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vuelta', models.IntegerField()),
                ('tiempo_total', models.DurationField()),
                ('tiempo_vuelta', models.DurationField()),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.Carreras')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.Equipos')),
            ],
        ),
    ]
