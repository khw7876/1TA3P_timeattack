# Generated by Django 4.0.5 on 2022-06-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rename_tag_name_postmodel_tag_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagmodel',
            name='tagname',
            field=models.CharField(max_length=20),
        ),
    ]
