# Generated by Django 3.2 on 2021-04-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DNASample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.TextField()),
                ('is_mutant', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mutant_samples', models.IntegerField()),
                ('human_samples', models.IntegerField()),
                ('ratio', models.FloatField()),
            ],
        ),
    ]