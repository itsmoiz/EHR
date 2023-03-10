# Generated by Django 4.0.6 on 2022-10-19 09:46

import BackEndApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BackEndApp', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('criticalLevel', models.TextField()),
                ('city', models.CharField(max_length=99)),
                ('doctor', models.CharField(max_length=99)),
                ('description', models.CharField(max_length=99999)),
                ('patient', models.CharField(max_length=99)),
                ('laboratory', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=300)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('criticalLevel', models.TextField()),
                ('description', models.CharField(max_length=99999)),
                ('patient', models.CharField(max_length=99)),
                ('doctor', models.CharField(max_length=99)),
                ('city', models.CharField(max_length=99)),
                ('hospital', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.TextField()),
                ('label', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=99999)),
                ('file', models.FileField(upload_to=BackEndApp.models.prescriptions)),
            ],
        ),
        migrations.CreateModel(
            name='ReportFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.TextField()),
                ('label', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=99999)),
                ('file', models.FileField(upload_to=BackEndApp.models.reports)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('name', models.CharField(max_length=999)),
                ('city', models.TextField()),
                ('license_No', models.TextField(primary_key=True, serialize=False)),
                ('branch_code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('name', models.CharField(max_length=999)),
                ('city', models.TextField()),
                ('license_No', models.TextField(primary_key=True, serialize=False)),
                ('branch_code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
