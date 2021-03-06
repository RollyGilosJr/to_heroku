# Generated by Django 3.2.7 on 2021-11-28 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submissions', '0008_remove_rubrix_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubrix',
            name='evaluator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rubrix',
            name='grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='rubrix',
            name='student_submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='submissions.studentsubmit'),
        ),
    ]
