# Generated by Django 4.2.8 on 2024-01-15 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='pumpInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pumpNumber', models.CharField(max_length=20)),
                ('vehicleNumber', models.CharField(max_length=50, null=True)),
                ('odometer', models.IntegerField(null=True)),
                ('pumpStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicleNumber', models.CharField(max_length=50)),
                ('vehicleId', models.CharField(max_length=50, unique=True)),
                ('gallonLimit', models.IntegerField()),
                ('odometer', models.IntegerField(null=True)),
                ('companyName', models.CharField(max_length=50)),
                ('productName', models.CharField(max_length=50)),
                ('totalGallon', models.IntegerField()),
                ('meteredHours', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleNumber', models.CharField(max_length=50, unique=True)),
                ('vehicleId', models.CharField(max_length=50, unique=True)),
                ('quantity', models.IntegerField(null=True)),
                ('gallonLimit', models.IntegerField()),
                ('odometer', models.IntegerField(null=True)),
                ('companyName', models.CharField(max_length=50)),
                ('productName', models.CharField(max_length=50)),
                ('totalGallon', models.IntegerField()),
                ('meteredHours', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]