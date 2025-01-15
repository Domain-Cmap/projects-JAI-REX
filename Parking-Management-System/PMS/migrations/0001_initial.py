# Generated by Django 3.2.7 on 2023-03-08 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=100)),
                ('total_floors', models.PositiveIntegerField(default=2)),
                ('total_rows', models.PositiveIntegerField(default=10)),
                ('total_coloumn', models.PositiveIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor_name', models.CharField(max_length=40)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.building')),
            ],
        ),
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Row_name', models.CharField(max_length=50)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.building')),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.floor')),
            ],
        ),
        migrations.CreateModel(
            name='Coloumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coloumn_name', models.CharField(max_length=40)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.building')),
                ('floor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.floor')),
                ('rows_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMS.rows')),
            ],
        ),
    ]