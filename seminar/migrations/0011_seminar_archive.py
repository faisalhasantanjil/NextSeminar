# Generated by Django 4.0.3 on 2023-07-20 20:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0010_alter_organization_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='archive',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='Not Posted Yet', null=True),
        ),
    ]
