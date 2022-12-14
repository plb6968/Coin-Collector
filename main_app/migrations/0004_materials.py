# Generated by Django 4.1.3 on 2022-11-21 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_coin_rarity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(choices=[('0', 'Silver'), ('1', 'Gold'), ('2', 'Copper'), ('3', 'Brass'), ('4', 'Zinc'), ('5', 'Nickel')], default='0', max_length=1)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coin')),
            ],
        ),
    ]
