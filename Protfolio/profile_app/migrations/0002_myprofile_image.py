# Generated by Django 4.2.5 on 2023-09-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/myPhotos'),
        ),
    ]
