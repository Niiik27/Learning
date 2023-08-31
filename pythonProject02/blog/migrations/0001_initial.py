# Generated by Django 4.2.4 on 2023-08-24 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('desc', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/image')),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
    ]