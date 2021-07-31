# Generated by Django 3.2.5 on 2021-07-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=150)),
                ('Post', models.CharField(blank=True, max_length=300, null=True)),
                ('Height', models.IntegerField(blank=True)),
                ('StateOfOrigin', models.CharField(blank=True, max_length=150)),
                ('DateOfBirth', models.DateField(blank=True)),
            ],
        ),
    ]
