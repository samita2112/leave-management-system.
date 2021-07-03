# Generated by Django 3.2 on 2021-06-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0009_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='enddate',
            field=models.DateTimeField(help_text='coming back on ...', null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='startdate',
            field=models.DateTimeField(help_text='leave start date is on ..', null=True, verbose_name='Start Date'),
        ),
    ]
