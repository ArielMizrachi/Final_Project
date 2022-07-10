# Generated by Django 3.2.8 on 2022-07-09 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Companies',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('flag', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('Departure_Time', models.DateTimeField(auto_now_add=True)),
                ('Landing_Time', models.DateTimeField(auto_now_add=True)),
                ('Remaining_Ticets', models.IntegerField(blank=True, null=True)),
                ('Airline_Company_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.airline_companies')),
                ('Destenation_Country_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('Origin_Country_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.countries')),
            ],
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='Country_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.countries'),
        ),
        migrations.AddField(
            model_name='airline_companies',
            name='User_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]