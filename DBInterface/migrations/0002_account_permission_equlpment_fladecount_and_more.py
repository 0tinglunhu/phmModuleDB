# Generated by Django 4.0.6 on 2022-08-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBInterface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='permission',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equlpment',
            name='fladeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equlpment',
            name='photo',
            field=models.TextField(default='//'),
        ),
        migrations.AddField(
            model_name='equlpment',
            name='power',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equlpment',
            name='rotationalSpeed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='physical_sensor_manager',
            name='battery',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='physical_sensor_manager',
            name='wifi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='machine',
            name='electric',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='machine',
            name='photo',
            field=models.TextField(default='//'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='power',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='machine',
            name='voltage',
            field=models.FloatField(default=0),
        ),
    ]
