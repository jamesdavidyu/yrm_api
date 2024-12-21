# Generated by Django 5.1 on 2024-12-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0006_alter_hour_hour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hour',
            old_name='hour',
            new_name='hour_value',
        ),
        migrations.AddField(
            model_name='hour',
            name='hour_label',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
