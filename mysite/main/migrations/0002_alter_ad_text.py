# Generated by Django 4.1.4 on 2022-12-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='text',
            field=models.CharField(max_length=800),
        ),
    ]