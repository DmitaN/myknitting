# Generated by Django 3.0.7 on 2020-06-12 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200613_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='productName',
        ),
    ]
