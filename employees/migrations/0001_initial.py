# Generated by Django 5.1.2 on 2024-10-18 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('is_fired', models.BooleanField(default=False)),
                ('date_of_termination', models.DateField(blank=True, null=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.position')),
            ],
        ),
    ]
