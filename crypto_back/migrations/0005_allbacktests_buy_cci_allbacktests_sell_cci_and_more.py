# Generated by Django 4.1.1 on 2022-10-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_back', '0004_allbacktests_hyperopt'),
    ]

    operations = [
        migrations.AddField(
            model_name='allbacktests',
            name='buy_cci',
            field=models.IntegerField(default=50, verbose_name='Buy side: CCI between -700 and 0:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allbacktests',
            name='sell_cci',
            field=models.IntegerField(default=100, verbose_name='Sell side: CCI between 0 and 700:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='arg_MR',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Movement ROI (MR)'),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='arg_P',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Price incriase in N candles (P)'),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='arg_stoploss',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Dsired Stop-loss value (S)'),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='minimal_roi1_value',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='minimal_roi2_value',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='minimal_roi3_value',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='minimal_roi4_value',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='my_stoploss_value',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='My Stop-loss value (after [n] min)'),
        ),
        migrations.AlterField(
            model_name='allbacktests',
            name='stoploss',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Stop-loss (after 0 min)'),
        ),
    ]
