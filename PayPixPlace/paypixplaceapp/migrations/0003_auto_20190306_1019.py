# Generated by Django 2.1.7 on 2019-03-06 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paypixplaceapp', '0002_auto_20190306_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paypixplaceapp.Role'),
        ),
    ]
