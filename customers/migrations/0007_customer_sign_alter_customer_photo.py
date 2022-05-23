# Generated by Django 4.0.2 on 2022-05-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_alter_customer_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='sign',
            field=models.ImageField(default=1, upload_to='sign/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
