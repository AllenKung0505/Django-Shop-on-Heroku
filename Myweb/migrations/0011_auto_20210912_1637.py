# Generated by Django 3.2.5 on 2021-09-12 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myweb', '0010_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_customaddress',
        ),
        migrations.RemoveField(
            model_name='user',
            name='u_customname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='u_customphone',
        ),
    ]
