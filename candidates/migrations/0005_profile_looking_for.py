# Generated by Django 3.1.1 on 2020-09-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_appliedjobs_savedjobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='looking_for',
            field=models.CharField(choices=[('full-time', 'Full Time'), ('part-time', 'Part Time'), ('intern', 'Internship'), ('remote', 'Remote')], default='full-time', max_length=30, null=True),
        ),
    ]
