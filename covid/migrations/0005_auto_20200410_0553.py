# Generated by Django 3.0.2 on 2020-04-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0004_auto_20200410_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='asymp',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='symptoms',
            name='health',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='symptoms',
            name='healthcond',
            field=models.CharField(choices=[(' Same as before', 'sameasbefore'), ('Improved', 'improved'), ('Worsened', 'worsened'), ('Worsened Considerably', 'worsenedconsiderably')], default='NoneOfThese', max_length=40, verbose_name='HealthCondition'),
        ),
        migrations.AlterField(
            model_name='symptoms',
            name='symp',
            field=models.CharField(max_length=40),
        ),
    ]
