# Generated by Django 4.2.9 on 2024-03-12 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('fees', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]