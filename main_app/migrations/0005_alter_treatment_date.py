# Generated by Django 4.2.7 on 2023-11-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_delete_bird_delete_cat_delete_dog_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
