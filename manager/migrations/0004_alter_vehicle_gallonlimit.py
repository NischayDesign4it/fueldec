# Generated by Django 4.2.8 on 2024-01-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_vehicle_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='gallonLimit',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
