# Generated by Django 3.2.20 on 2023-07-30 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20230730_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_basket',
        ),
    ]
