# Generated by Django 3.2.22 on 2023-10-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_vote', '0009_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date',
            field=models.DateField(default='2023-10-24'),
            preserve_default=False,
        ),
    ]
