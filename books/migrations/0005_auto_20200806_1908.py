# Generated by Django 3.0.8 on 2020-08-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200806_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]