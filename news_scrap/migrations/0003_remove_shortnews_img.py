# Generated by Django 2.0.6 on 2018-06-27 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_scrap', '0002_auto_20180626_0524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortnews',
            name='img',
        ),
    ]
