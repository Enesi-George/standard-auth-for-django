# Generated by Django 4.2.4 on 2023-09-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('physical_storage', '0014_alter_physcialstorageform_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physcialstorageform',
            name='items',
        ),
    ]
