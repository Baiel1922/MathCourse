# Generated by Django 4.1.7 on 2023-04-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]