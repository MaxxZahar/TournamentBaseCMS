# Generated by Django 3.2.14 on 2022-09-12 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_page', '0001_initial'),
        ('tournaments', '0004_alter_playermodel_tournaments'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerCardPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='garpix_page.basepage')),
            ],
            options={
                'verbose_name': 'Профиль игрока',
                'verbose_name_plural': 'Профили игроков',
                'ordering': ('-created_at',),
            },
            bases=('garpix_page.basepage',),
        ),
    ]