# Generated by Django 2.2.3 on 2019-08-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0003_auto_20190817_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_urls',
            name='short_url',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
