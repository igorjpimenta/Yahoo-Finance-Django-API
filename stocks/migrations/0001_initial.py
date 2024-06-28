# Generated by Django 5.0.6 on 2024-06-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IssuedTickers',
            fields=[
                ('id_issued_ticker', models.AutoField(primary_key=True, serialize=False)),
                ('ticker', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'tb_issued_ticker',
            },
        ),
    ]
