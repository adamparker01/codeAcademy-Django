# Generated by Django 4.2.6 on 2023-10-17 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vetoffice', '0002_alter_patient_options_alter_patient_pet_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='user',
        ),
    ]
