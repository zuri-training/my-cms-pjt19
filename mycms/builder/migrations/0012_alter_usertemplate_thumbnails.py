# Generated by Django 4.1 on 2022-08-12 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0011_alter_usertemplate_thumbnails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertemplate',
            name='thumbnails',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
