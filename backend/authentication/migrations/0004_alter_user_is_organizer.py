# Generated by Django 4.0.4 on 2022-05-25 16:59

import branch.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_is_user_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_organizer',
            field=models.BooleanField(default=False, verbose_name=branch.models.Branch),
        ),
    ]
