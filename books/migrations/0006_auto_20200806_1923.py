# Generated by Django 3.0.8 on 2020-08-06 22:23

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200806_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=stdimage.models.StdImageField(upload_to='static/img'),
        ),
    ]
