# Generated by Django 3.2.7 on 2021-09-07 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myweb', '0003_alter_product_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_description',
            field=models.CharField(default='', max_length=80),
        ),
    ]
