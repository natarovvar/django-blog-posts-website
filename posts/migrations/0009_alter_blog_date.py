# Generated by Django 4.1.7 on 2023-03-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_title_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
