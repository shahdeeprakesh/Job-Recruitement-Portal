# Generated by Django 3.1.1 on 2020-09-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0010_auto_20200919_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='skills_req',
            field=models.CharField(max_length=200),
        ),
    ]
