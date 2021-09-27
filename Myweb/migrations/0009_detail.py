# Generated by Django 3.2.7 on 2021-09-11 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myweb', '0008_auto_20210909_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_product', models.CharField(default='', max_length=100)),
                ('d_unitprice', models.IntegerField(default=0)),
                ('d_quantity', models.IntegerField(default=0)),
                ('d_total', models.IntegerField(default=0)),
                ('d_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myweb.order')),
            ],
            options={
                'db_table': 'Detail',
            },
        ),
    ]