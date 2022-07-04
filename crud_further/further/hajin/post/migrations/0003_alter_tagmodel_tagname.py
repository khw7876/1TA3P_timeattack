# Generated by Django 4.0.5 on 2022-06-22 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_tagmodel_postmodel_title_postmodel_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagmodel',
            name='tagname',
            field=models.CharField(choices=[('D', 'day'), ('S', 'sports'), ('F', 'food'), ('N', 'news')], max_length=20),
        ),
    ]
