# Generated by Django 3.2.7 on 2021-11-28 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manuscriptevaluations', '0005_auto_20211129_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluationgrade',
            name='submission_title',
        ),
    ]
