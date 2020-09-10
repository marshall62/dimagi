# Generated by Django 3.1.1 on 2020-09-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
