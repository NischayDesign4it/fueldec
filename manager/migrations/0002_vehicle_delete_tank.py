# Generated by Django 4.2.8 on 2023-12-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleNumber', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField(null=True)),
                ('odometer', models.IntegerField(null=True)),
                ('last_dispensed_quantity', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tank',
        ),
    ]
