# Generated by Django 3.1.3 on 2020-11-23 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50, unique=True)),
                ('course_information', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentcourseapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentcourseapp.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='unique_first_name_last_name'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='studentcourseapp.StudentCourse', to='studentcourseapp.Student'),
        ),
    ]
