# Generated by Django 3.1.1 on 2020-09-19 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_auto_20200919_0835'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjobs',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='savedjobs',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
