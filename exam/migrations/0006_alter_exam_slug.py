# Generated by Django 4.0.2 on 2022-11-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_remove_exam_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
