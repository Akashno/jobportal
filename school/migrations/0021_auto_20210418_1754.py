# Generated by Django 3.0.5 on 2021-04-18 12:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0020_delete_attendance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeacherExtra',
            new_name='RecruterExtra',
        ),
    ]
