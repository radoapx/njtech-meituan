# Generated by Django 2.2.4 on 2019-09-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_end_app', '0010_customer_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping_cart',
            name='isdeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shopping_cart',
            name='isselected',
            field=models.BooleanField(default=True),
        ),
    ]
