# Generated by Django 4.2.4 on 2023-08-25 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('physical_storage', '0006_remove_physcialstorageform_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physcialstorageform',
            name='dimension_of_storage',
        ),
        migrations.AddField(
            model_name='physcialstorageform',
            name='dimension_of_storage_with_price',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='physical_storage.dimensionprice'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='physcialstorageform',
            name='choose_a_storage_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physical_storage.physicalstorage'),
        ),
    ]
