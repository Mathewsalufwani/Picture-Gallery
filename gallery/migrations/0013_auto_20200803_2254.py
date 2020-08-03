# Generated by Django 3.0.8 on 2020-08-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20200803_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photos',
            old_name='descriptio',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='photos',
            name='tag',
            field=models.ManyToManyField(to='gallery.Tag'),
        ),
    ]