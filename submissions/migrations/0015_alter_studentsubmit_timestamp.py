# Generated by Django 3.2.7 on 2021-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0014_studentsubmit_eval_grade_submit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsubmit',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
