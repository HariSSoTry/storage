# Generated by Django 5.0.4 on 2024-04-25 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_card', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='documents',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='additional_documents',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='patientdatabase',
            name='patients',
        ),
        migrations.RemoveField(
            model_name='patientdatabase',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='author',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='symptom',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Folder',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='PatientDatabase',
        ),
    ]
