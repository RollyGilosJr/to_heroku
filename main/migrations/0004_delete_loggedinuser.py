# Generated by Django 3.2.7 on 2022-01-04 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_loggedinuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoggedInUser',
        ),
    ]
