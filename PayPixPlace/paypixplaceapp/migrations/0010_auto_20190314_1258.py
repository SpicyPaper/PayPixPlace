# Generated by Django 2.1.7 on 2019-03-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypixplaceapp', '0009_auto_20190313_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_ammo_usage',
            field=models.DateField(null=True),
        ),
    ]
