# Generated by Django 3.2.5 on 2022-03-10 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icyl_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agegroup',
            options={'ordering': ['id']},
        ),
    ]