# Generated by Django 3.2.7 on 2021-10-08 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('1', 'Dean'), ('2', 'Capstone Professor'), ('3', 'Faculty'), ('4', 'Student')], default='3', max_length=100)),
                ('image', models.ImageField(default='profiles/user.png', upload_to='profiles/')),
                ('group_name', models.CharField(default='None', max_length=250)),
                ('group_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('mem1_fn', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem1_ln', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem1_email', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem2_fn', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem2_ln', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem2_email', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem3_fn', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem3_ln', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem3_email', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem4_fn', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem4_ln', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('mem4_email', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('group_title', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('group_adviser', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adviser', to=settings.AUTH_USER_MODEL)),
                ('group_panel_1', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='panel1', to=settings.AUTH_USER_MODEL)),
                ('group_panel_2', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='panel2', to=settings.AUTH_USER_MODEL)),
                ('group_panel_3', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='panel3', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
