# Generated by Django 4.1.6 on 2023-03-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_wlosy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wstep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('waga', models.DecimalField(decimal_places=8, max_digits=8)),
                ('wzrost', models.DecimalField(decimal_places=8, max_digits=8)),
                ('wiek', models.DecimalField(decimal_places=8, max_digits=8)),
            ],
        ),
    ]
