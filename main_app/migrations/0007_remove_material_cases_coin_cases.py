# Generated by Django 4.1.3 on 2022-11-22 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_case_material_cases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='cases',
        ),
        migrations.AddField(
            model_name='coin',
            name='cases',
            field=models.ManyToManyField(to='main_app.case'),
        ),
    ]
