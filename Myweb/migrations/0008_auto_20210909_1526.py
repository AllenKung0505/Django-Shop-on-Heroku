# Generated by Django 3.2.7 on 2021-09-09 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myweb', '0007_auto_20210909_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='o_costumaddress',
            new_name='o_customaddress',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='o_costumname',
            new_name='o_customname',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='o_costumphone',
            new_name='o_customphone',
        ),
    ]
