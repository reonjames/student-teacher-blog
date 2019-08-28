# Generated by Django 2.0.6 on 2019-08-18 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=15)),
                ('bio', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('eng', models.IntegerField()),
                ('chem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('standard', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Academic')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
        ),
    ]
