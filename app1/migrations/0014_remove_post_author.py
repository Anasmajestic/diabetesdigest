# Generated by Django 5.0.1 on 2024-02-07 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]