# Generated by Django 2.0.7 on 2018-08-06 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_scrap', '0005_auto_20180806_0954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortnews',
            old_name='lid',
            new_name='full_text',
        ),
        migrations.RemoveField(
            model_name='shortnews',
            name='author',
        ),
    ]
