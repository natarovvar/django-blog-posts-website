# Generated by Django 4.1.7 on 2023-03-21 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name=datetime.datetime(2023, 3, 21, 16, 1, 13, 922252, tzinfo=datetime.timezone.utc)),
        ),
    ]