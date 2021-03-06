# Generated by Django 2.2.7 on 2020-03-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_apk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'fundacja'), (2, 'organizacja pozarządowa'), (3, 'zbiórka lokalna')], default=1)),
                ('categories', models.ManyToManyField(to='main_apk.CategoryModel')),
            ],
        ),
    ]
