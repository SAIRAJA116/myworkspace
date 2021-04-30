# Generated by Django 3.1 on 2020-09-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Qualifications', models.CharField(blank=True, max_length=20, null=True)),
                ('Department', models.CharField(choices=[('ece', 'ECE'), ('cse', 'CSE'), ('it', 'IT'), ('me', 'ME'), ('ce', 'CIVIL')], max_length=10)),
                ('Email', models.EmailField(default='abc@gmail.com', max_length=254)),
                ('Phone', models.CharField(help_text='8919227696', max_length=10)),
            ],
        ),
    ]
