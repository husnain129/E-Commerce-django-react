# Generated by Django 3.0.8 on 2020-09-13 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
