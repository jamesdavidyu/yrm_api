# Generated by Django 5.1 on 2024-12-20 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_hour_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='hour',
            field=models.DecimalField(decimal_places=2, max_digits=4, unique=True),
        ),
    ]