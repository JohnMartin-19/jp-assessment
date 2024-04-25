# Generated by Django 5.0.4 on 2024-04-25 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('registration_date', models.DateField()),
                ('location', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(choices=[('FinTech', 'FinTech'), ('Learning Institute', 'Learning Institute'), ('Transportation', 'Transportation'), ('Service', 'Service'), ('Banking', 'Banking')], max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers')),
            ],
        ),
    ]