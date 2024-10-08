# Generated by Django 5.1.1 on 2024-09-12 01:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedLGAResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_abbreviation', models.CharField(max_length=3)),
                ('party_score', models.IntegerField()),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec_app.lga')),
            ],
        ),
        migrations.CreateModel(
            name='AnnouncedPUResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_abbreviation', models.CharField(max_length=3)),
                ('party_score', models.IntegerField()),
                ('polling_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec_app.pollingunit')),
            ],
        ),
        migrations.AddField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec_app.state'),
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec_app.lga')),
            ],
        ),
        migrations.AddField(
            model_name='pollingunit',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inec_app.ward'),
        ),
    ]
