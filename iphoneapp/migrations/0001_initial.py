# Generated by Django 3.2 on 2021-05-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('adminemailid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('adminpassword', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Admins',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('custname', models.CharField(max_length=50)),
                ('custemail', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('custpassword', models.CharField(max_length=50)),
                ('custcontact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('storeid', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
                ('image', models.FileField(upload_to='iphoneapp/images/')),
            ],
            options={
                'db_table': 'Store',
            },
        ),
    ]