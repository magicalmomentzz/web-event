# Generated by Django 4.1 on 2022-08-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_eventregisterform_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregisterform',
            name='amount',
            field=models.IntegerField(max_length=11111),
        ),
    ]
