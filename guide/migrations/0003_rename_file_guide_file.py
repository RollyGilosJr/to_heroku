# Generated by Django 3.2.7 on 2021-12-14 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_rename_pdf_guide_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='file',
            new_name='File',
        ),
    ]
