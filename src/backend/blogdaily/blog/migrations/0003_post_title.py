# Generated by Django 4.0.3 on 2022-04-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_authors_author_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]
