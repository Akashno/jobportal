# Generated by Django 3.0.5 on 2021-04-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='university',
            field=models.CharField(default='calicut', max_length=300),
            preserve_default=False,
        ),
    ]