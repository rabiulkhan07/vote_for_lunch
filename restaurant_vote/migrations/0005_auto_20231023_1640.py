# Generated by Django 3.2.22 on 2023-10-23 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_vote', '0004_remove_restaurant_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voted_by',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
