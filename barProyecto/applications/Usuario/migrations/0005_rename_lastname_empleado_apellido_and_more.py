# Generated by Django 4.1.9 on 2023-05-19 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0004_rename_apellidos_empleado_lastname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='lastname',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='mail',
            new_name='clave',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='name',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='password',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='sedeId',
            new_name='sede_id',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='phone',
            new_name='telefono',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='rolId',
            new_name='tipo_empleado_id',
        ),
    ]
