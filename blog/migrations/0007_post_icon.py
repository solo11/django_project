# Generated by Django 2.2.3 on 2019-08-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_catg'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icon',
            field=models.CharField(default='book', max_length=10),
        ),
    ]