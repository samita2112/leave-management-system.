# Generated by Django 3.2 on 2021-04-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20210420_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminn',
            name='roll_no',
        ),
    ]
