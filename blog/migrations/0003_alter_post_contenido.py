# Generated by Django 4.1.4 on 2022-12-28 09:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="contenido",
            field=ckeditor.fields.RichTextField(verbose_name="Contenido"),
        ),
    ]
