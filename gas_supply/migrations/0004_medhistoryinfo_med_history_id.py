# Generated by Django 2.2.6 on 2019-10-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_supply', '0003_auto_20191022_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='medhistoryinfo',
            name='med_history_id',
            field=models.IntegerField(default=0),
        ),
    ]
