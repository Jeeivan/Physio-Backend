# Generated by Django 4.2.7 on 2024-01-31 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_discussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='name',
            field=models.CharField(default=True),
            preserve_default=False,
        ),
    ]
