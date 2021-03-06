# Generated by Django 3.0.8 on 2020-07-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wuliu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.CharField(max_length=10, unique=True)),
                ('num2', models.CharField(max_length=10, unique=True)),
                ('product_name', models.CharField(default='', max_length=1000)),
                ('logistics_name', models.CharField(default='', max_length=1000)),
                ('sale_name', models.CharField(default='', max_length=1000)),
                ('product_address', models.CharField(default='', max_length=1000)),
                ('logistics_address', models.CharField(default='', max_length=1000)),
                ('sale_address', models.CharField(default='', max_length=1000)),
                ('product_time', models.CharField(default='', max_length=1000)),
                ('logistics_time', models.CharField(default='', max_length=1000)),
                ('sale_time', models.CharField(default='', max_length=1000)),
                ('information', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]
