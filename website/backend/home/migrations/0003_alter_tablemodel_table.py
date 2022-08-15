# Generated by Django 3.2.14 on 2022-08-15 14:33

from django.db import migrations, models
import home.validators.file_extension_validator


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tablemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemodel',
            name='table',
            field=models.FileField(upload_to='', validators=[home.validators.file_extension_validator.validate_file_extension], verbose_name='Файл с таблицей'),
        ),
    ]