# Generated by Django 3.2.7 on 2021-11-14 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(default='F40AAF', max_length=6),
        ),
    ]
