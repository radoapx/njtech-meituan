# Generated by Django 2.2.4 on 2019-09-11 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_end_app', '0014_auto_20190911_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_phone',
            field=models.IntegerField(verbose_name=1000000000000),
        ),
    ]
