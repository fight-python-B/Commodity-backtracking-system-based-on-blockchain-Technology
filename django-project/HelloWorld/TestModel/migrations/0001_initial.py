# Generated by Django 3.0.7 on 2020-07-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('productNumber', models.CharField(max_length=20)),
                ('producerName', models.CharField(max_length=20)),
                ('StartTime', models.CharField(max_length=20)),
                ('TransforName', models.CharField(max_length=20)),
                ('TransforTime', models.CharField(max_length=20)),
                ('SaleName', models.CharField(max_length=20)),
                ('SaleTime', models.CharField(max_length=20)),
            ],
        ),
    ]