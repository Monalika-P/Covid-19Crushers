# Generated by Django 3.0.2 on 2020-04-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0005_auto_20200410_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help1',
            name='supply',
            field=models.CharField(choices=[('FOOD', 'Food'), ('SUPPLY', 'Supply'), ('BOTH', 'Both')], default='Food', max_length=15, verbose_name='Supplies'),
        ),
    ]
