# Generated by Django 4.1.1 on 2023-01-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_back', '0010_allbacktests_start_data_allbacktests_stop_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allbacktests',
            name='start_data',
            field=models.DateField(auto_now_add=True, verbose_name='Strat data'),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='stop_data',
            field=models.DateField(auto_now_add=True, verbose_name='Stop data'),
        ),
    ]
