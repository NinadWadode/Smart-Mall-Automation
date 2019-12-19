# Generated by Django 2.2.6 on 2019-12-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartMall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.IntegerField()),
                ('dist', models.FloatField()),
            ],
            options={
                'db_table': 'parking',
            },
        ),
    ]