# Generated by Django 4.1.1 on 2022-10-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_back', '0003_allbacktests_max_open_trades_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allbacktests',
            name='hyperopt',
            field=models.BooleanField(default=False, verbose_name='Hyper opt'),
            preserve_default=False,
        ),
    ]
