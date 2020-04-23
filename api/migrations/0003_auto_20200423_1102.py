# Generated by Django 3.0.4 on 2020-04-23 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200422_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('infected_count', models.IntegerField(default=0)),
                ('recovered_count', models.IntegerField(default=0)),
                ('died_count', models.IntegerField(default=0)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('infected_count', models.IntegerField(default=0)),
                ('recovered_count', models.IntegerField(default=0)),
                ('died_count', models.IntegerField(default=0)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Country')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Region')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.City'),
        ),
        migrations.AddField(
            model_name='person',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Region'),
        ),
    ]
