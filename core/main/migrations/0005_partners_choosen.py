# Generated by Django 5.1.5 on 2025-02-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_partners_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='choosen',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
