# Generated by Django 2.2.5 on 2019-09-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=220),
        ),
    ]
