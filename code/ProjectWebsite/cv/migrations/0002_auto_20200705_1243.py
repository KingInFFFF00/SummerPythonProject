# Generated by Django 2.2.13 on 2020-07-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationhistory',
            name='title',
            field=models.CharField(default='title', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalachievement',
            name='title',
            field=models.CharField(default='title', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workhistory',
            name='title',
            field=models.CharField(default='title', max_length=30),
            preserve_default=False,
        ),
    ]
