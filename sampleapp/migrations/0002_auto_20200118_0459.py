# Generated by Django 3.0.2 on 2020-01-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=10, verbose_name='ユーザ'),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=10, verbose_name='ユーザ'),
        ),
    ]
