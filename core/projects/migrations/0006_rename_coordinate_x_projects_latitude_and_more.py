# Generated by Django 5.1.5 on 2025-02-18 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_projects_coordinate_x_projects_coordinate_y_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='coordinate_x',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='coordinate_y',
            new_name='longitude',
        ),
    ]
