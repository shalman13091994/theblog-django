# Generated by Django 3.1.4 on 2021-08-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210819_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default_pic.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
