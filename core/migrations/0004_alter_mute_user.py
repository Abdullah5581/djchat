# Generated by Django 5.1.1 on 2024-12-13 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_mute_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mute',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mute', to='core.profile'),
        ),
    ]