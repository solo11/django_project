# Generated by Django 2.2.3 on 2019-07-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190725_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='static/images/default_cover.jpg', upload_to='cover/'),
        ),
    ]
