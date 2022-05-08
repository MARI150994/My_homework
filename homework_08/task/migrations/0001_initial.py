# Generated by Django 4.0.3 on 2022-04-08 17:16

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
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Department name')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description of department')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name of project')),
                ('description', models.CharField(max_length=300, verbose_name='Description of project')),
                ('status', models.CharField(choices=[('In work', 'In work'), ('Canceled', 'Canceled'), ('Finished', 'Finished'), ('Awaiting', 'Awaiting')], max_length=40, verbose_name='Status of project')),
                ('priority', models.CharField(choices=[('Very high', 'Very important'), ('High', 'High'), ('Middle', 'Middle'), ('Low', 'Low'), ('Very low', 'Very low')], max_length=40, verbose_name='Priority of project')),
                ('planned_date', models.DateTimeField(verbose_name='Planned end date')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name='Time when project was created')),
                ('finish_date', models.DateTimeField(null=True, verbose_name='Time when project was finished or closed')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Users hwo can delegate this project, update and eg')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Name of task')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description of task')),
                ('planned_date', models.DateTimeField(verbose_name='How much time is allocated for the task')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name='Time when task was started')),
                ('finish_date', models.DateTimeField(null=True, verbose_name='Time when task was finished')),
                ('status', models.CharField(choices=[('In work', 'In work'), ('Canceled', 'Canceled'), ('Finished', 'Finished'), ('Awaiting', 'Awaiting')], max_length=40, verbose_name='Status of task')),
                ('priority', models.CharField(choices=[('Very high', 'Very important'), ('High', 'High'), ('Middle', 'Middle'), ('Low', 'Low'), ('Very low', 'Very low')], max_length=40, verbose_name='Priority of task')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Executor of this task')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.project')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Position name')),
                ('is_header', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='roles', to='task.department', verbose_name='Position department name')),
            ],
        ),
    ]