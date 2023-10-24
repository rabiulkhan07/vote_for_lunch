# Generated by Django 3.2.22 on 2023-10-23 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant_vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='items',
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='', upload_to='menu_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
            preserve_default=False,
        ),
    ]
