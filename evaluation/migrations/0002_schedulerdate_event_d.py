# Generated by Django 3.2.7 on 2021-10-09 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulerdate',
            name='event_d',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='event_d', to='evaluation.schedulerevent'),
        ),
    ]
