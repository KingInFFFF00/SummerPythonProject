# Generated by Django 2.2.13 on 2020-07-05 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200705_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationhistory',
            name='title',
        ),
        migrations.RemoveField(
            model_name='personalachievement',
            name='title',
        ),
        migrations.RemoveField(
            model_name='workhistory',
            name='title',
        ),
    ]
