# Generated by Django 3.1.7 on 2021-03-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]
