# Generated by Django 3.2 on 2021-06-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_auto_20210621_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='dept_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
