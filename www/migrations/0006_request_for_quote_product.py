# Generated by Django 4.1.7 on 2023-06-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_request_for_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_for_quote',
            name='product',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
