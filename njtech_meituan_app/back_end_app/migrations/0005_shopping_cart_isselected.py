# Generated by Django 2.2.4 on 2019-09-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_end_app', '0004_auto_20190903_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='isselected',
            field=models.BooleanField(default=False),
        ),
    ]