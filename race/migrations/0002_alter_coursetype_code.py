# Generated by Django 5.2 on 2025-05-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetype',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
