# Generated by Django 2.2.7 on 2020-03-30 07:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_apk', '0005_auto_20200330_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationmodel',
            name='last_mod',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
