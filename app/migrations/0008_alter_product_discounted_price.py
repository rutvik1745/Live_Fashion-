# Generated by Django 4.2 on 2023-04-21 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_customer_address_alter_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.IntegerField(null=True),
        ),
    ]
