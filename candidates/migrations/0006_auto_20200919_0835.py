# Generated by Django 3.1.1 on 2020-09-19 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_profile_looking_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='looking_for',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Remote', 'Remote')], default='Full Time', max_length=30, null=True),
        ),
    ]
