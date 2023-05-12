# Generated by Django 4.0.9 on 2023-03-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectID', models.IntegerField()),
                ('nameEN', models.CharField(max_length=250)),
                ('nameTR', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
