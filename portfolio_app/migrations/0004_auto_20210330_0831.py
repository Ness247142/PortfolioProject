# Generated by Django 3.1.7 on 2021-03-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_remove_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default='A web development project.', max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.CharField(default='Django', max_length=200),
        ),
    ]
