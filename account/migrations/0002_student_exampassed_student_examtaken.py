# Generated by Django 4.0.2 on 2022-11-20 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='exampassed',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='examtaken',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
