# Generated by Django 3.0.7 on 2020-06-12 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200613_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='title',
        ),
    ]