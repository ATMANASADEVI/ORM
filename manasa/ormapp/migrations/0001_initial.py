# Generated by Django 5.1.2 on 2024-10-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankloan',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Accountno', models.IntegerField(primary_key='Accountno', serialize=False)),
                ('Interest', models.FloatField()),
                ('Startdate', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Mobilenumber', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('Enddate', models.DateField()),
            ],
        ),
    ]
