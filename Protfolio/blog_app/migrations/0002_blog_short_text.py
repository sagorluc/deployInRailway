# Generated by Django 4.2.5 on 2023-09-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_text',
            field=models.CharField(max_length=150, null=True),
        ),
    ]