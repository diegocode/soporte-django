# Generated by Django 4.0.4 on 2022-04-24 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('H', 'Hardware'), ('S', 'Software'), ('C', 'Conectividad'), ('I', 'Insumos'), ('X', 'Otro')], default='X', max_length=1)),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=120)),
                ('telefono', models.CharField(max_length=60)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Cerrado'), ('E', 'En curso')], default='P', max_length=1)),
                ('descripcion', models.CharField(default='', max_length=250)),
                ('fecha_reporte', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_resuelto', models.DateTimeField()),
            ],
            options={
                'ordering': ('-fecha_reporte',),
            },
        ),
    ]
