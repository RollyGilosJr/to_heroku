# Generated by Django 3.2.7 on 2021-11-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_code_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(default='ZX3FU', max_length=6, unique=True),
        ),
    ]
