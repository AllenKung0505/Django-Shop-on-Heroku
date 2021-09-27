# Generated by Django 3.2.5 on 2021-09-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myweb', '0009_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(default='', max_length=20)),
                ('u_password', models.CharField(default='', max_length=20)),
                ('u_customname', models.CharField(default='', max_length=50)),
                ('u_customphone', models.CharField(default='', max_length=50)),
                ('u_customaddress', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]