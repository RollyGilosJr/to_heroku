# Generated by Django 3.2.7 on 2021-11-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0013_delete_rubrix'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsubmit',
            name='eval_grade_submit',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
