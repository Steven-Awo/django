# Generated by Django 3.2.5 on 2021-07-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pages_number', models.IntegerField(blank=True, null=True)),
                ('publish_date', models.DateField()),
                ('author_name', models.CharField(max_length=150)),
            ],
        ),
    ]