# Generated by Django 4.1.9 on 2023-05-18 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sede', '0003_delete_precio'),
        ('Provedor', '0003_delete_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_venta', models.DecimalField(decimal_places=0, max_digits=15)),
                ('precio_compra', models.DecimalField(decimal_places=0, max_digits=15)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_final', models.DateTimeField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sede.producto')),
                ('proveedor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Provedor.proveedor')),
            ],
        ),
    ]