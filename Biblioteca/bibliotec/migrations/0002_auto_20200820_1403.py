# Generated by Django 2.2 on 2020-08-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='numLibros',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=30),
        ),
    ]