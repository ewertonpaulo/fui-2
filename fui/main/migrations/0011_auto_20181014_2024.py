# Generated by Django 2.1.1 on 2018-10-14 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20181014_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
