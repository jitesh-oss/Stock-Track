# Generated by Django 3.2.6 on 2022-02-04 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alertsmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('al_exchange_name', models.CharField(max_length=50)),
                ('al_type', models.CharField(max_length=50)),
                ('al_name', models.CharField(max_length=255)),
                ('al_code', models.CharField(max_length=50)),
                ('al_triggerprice', models.FloatField()),
                ('al_ltp', models.FloatField()),
                ('al_condition', models.CharField(max_length=255)),
                ('al_note', models.TextField()),
                ('al_user_id', models.IntegerField()),
                ('al_last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-al_last_updated',),
            },
        ),
        migrations.CreateModel(
            name='Categorymain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=50)),
                ('cat_desc', models.CharField(max_length=255)),
                ('cat_userid', models.TextField()),
                ('cat_createdon', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-cat_createdon',),
            },
        ),
        migrations.CreateModel(
            name='Journalmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jou_category', models.CharField(max_length=50)),
                ('jou_exchange', models.CharField(max_length=50)),
                ('jou_name', models.CharField(max_length=50)),
                ('jou_position', models.CharField(max_length=50)),
                ('jou_buydatetime', models.DateTimeField()),
                ('jou_buyprice', models.FloatField()),
                ('jou_buyqty', models.FloatField()),
                ('jou_selldatetime', models.DateTimeField()),
                ('jou_sellprice', models.FloatField()),
                ('jou_sellqty', models.FloatField()),
                ('jou_pl', models.FloatField()),
                ('jou_status', models.CharField(max_length=50)),
                ('jou_note', models.TextField()),
                ('jou_catid', models.IntegerField()),
                ('jou_userid', models.IntegerField()),
                ('jou_createdon', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-jou_buydatetime',),
            },
        ),
        migrations.CreateModel(
            name='Stocksmain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange_name', models.CharField(max_length=50)),
                ('st_type', models.CharField(max_length=50)),
                ('st_name', models.CharField(max_length=255)),
                ('st_code', models.CharField(max_length=50)),
                ('st_position', models.CharField(max_length=50)),
                ('st_buyprice', models.FloatField()),
                ('st_targetprice', models.FloatField()),
                ('st_stoploss', models.FloatField()),
                ('st_ltp', models.FloatField()),
                ('bought_on', models.DateField(default=django.utils.timezone.now)),
                ('user_id', models.IntegerField()),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-bought_on',),
            },
        ),
    ]
