# Generated by Django 4.2.6 on 2023-10-07 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='short_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='short_name'),
        ),
    ]