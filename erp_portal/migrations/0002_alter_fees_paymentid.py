# Generated by Django 3.2.4 on 2021-11-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='paymentid',
            field=models.CharField(blank=True, default=0, max_length=100),
        ),
    ]
