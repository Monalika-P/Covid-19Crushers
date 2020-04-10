# Generated by Django 3.0.2 on 2020-04-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('Other', 'Other')], default='MALE', max_length=20, verbose_name='Gender'),
        ),
    ]