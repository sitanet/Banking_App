# Generated by Django 4.0.2 on 2022-05-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_alter_customer_sign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sign',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
