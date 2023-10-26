# Generated by Django 4.2.4 on 2023-08-17 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('physical_storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensionPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimension', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('storage_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physical_storage.physicalstorage')),
            ],
        ),
    ]
