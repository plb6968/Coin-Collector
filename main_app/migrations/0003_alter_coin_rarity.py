# Generated by Django 4.1.3 on 2022-11-18 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_coin_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='rarity',
            field=models.CharField(max_length=150),
        ),
    ]
