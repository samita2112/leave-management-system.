# Generated by Django 3.2 on 2021-06-21 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20210429_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Employee', serialize=False, to='classroom.user')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('dept_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.department')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Manager', serialize=False, to='classroom.user')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('dept_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.department')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.RemoveField(
            model_name='studentmarks',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentmarks',
            name='teacher',
        ),
        migrations.AlterUniqueTogether(
            name='studentsinclass',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='studentsinclass',
            name='student',
        ),
        migrations.RemoveField(
            model_name='studentsinclass',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='submitassignment',
            name='student',
        ),
        migrations.RemoveField(
            model_name='submitassignment',
            name='submitted_assignment',
        ),
        migrations.RemoveField(
            model_name='submitassignment',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='class_students',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_student',
            new_name='is_employee',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_manager',
        ),
        migrations.DeleteModel(
            name='ClassAssignment',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentMarks',
        ),
        migrations.DeleteModel(
            name='StudentsInClass',
        ),
        migrations.DeleteModel(
            name='SubmitAssignment',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
