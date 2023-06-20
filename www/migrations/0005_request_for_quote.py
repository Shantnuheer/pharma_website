# Generated by Django 4.1.7 on 2023-06-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='request_for_quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('package', models.CharField(max_length=70)),
                ('weight', models.CharField(choices=[('MG', 'MG'), ('G', 'G'), ('KG', 'KG')], default='MG', max_length=100)),
            ],
        ),
    ]
