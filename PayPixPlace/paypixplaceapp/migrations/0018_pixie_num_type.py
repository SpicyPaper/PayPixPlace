# Generated by Django 2.1.7 on 2019-03-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypixplaceapp', '0017_merge_20190326_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='pixie',
            name='num_type',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
