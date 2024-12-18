# Generated by Django 5.1 on 2024-12-18 23:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_alter_name_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('input_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='name',
            old_name='created_at',
            new_name='input_at',
        ),
    ]
