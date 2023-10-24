# Generated by Django 3.2.22 on 2023-10-23 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant_vote', '0005_auto_20231023_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
            preserve_default=False,
        ),
    ]