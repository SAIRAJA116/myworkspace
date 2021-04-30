# Generated by Django 3.1 on 2020-09-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Number', models.IntegerField()),
                ('Book_Name', models.CharField(max_length=50)),
                ('Book_Author', models.CharField(max_length=50)),
                ('Department', models.CharField(choices=[('CSE', 'cse'), ('IT', 'it'), ('EEE', 'eee'), ('ECE', 'ece'), ('MECH', 'mech'), ('CIVIL', 'civil')], max_length=10)),
                ('Publication_Date', models.DateField()),
            ],
        ),
    ]