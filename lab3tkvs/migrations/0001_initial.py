# Generated by Django 4.2 on 2023-04-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Own',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('package', models.IntegerField()),
                ('drug', models.CharField(max_length=120)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]
