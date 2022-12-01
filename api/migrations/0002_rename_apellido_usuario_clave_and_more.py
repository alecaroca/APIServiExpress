# Generated by Django 4.1.2 on 2022-12-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='clave',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='direccionCom',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fnacimiento',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefonoCom',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
    ]