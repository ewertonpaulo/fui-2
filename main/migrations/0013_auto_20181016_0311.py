# Generated by Django 2.1.1 on 2018-10-16 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20181015_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='event_rated',
        ),
        migrations.AddField(
            model_name='rating',
            name='rated',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
