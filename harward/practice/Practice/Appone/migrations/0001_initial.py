# Generated by Django 3.1 on 2020-12-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('rollno', models.CharField(max_length=10)),
                ('percentage', models.IntegerField()),
            ],
        ),
    ]