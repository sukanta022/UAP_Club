# Generated by Django 5.2 on 2025-05-02 06:10

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_clubpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='clubpost',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
