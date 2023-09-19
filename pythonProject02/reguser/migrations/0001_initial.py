# Generated by Django 4.2.4 on 2023-09-19 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, verbose_name='Имя')),
                ('secondname', models.TextField(max_length=20, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('about', models.TextField(blank=True, verbose_name='О себе')),
                ('image_profile', models.ImageField(upload_to='profile/image/', verbose_name='Аватарка')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'readable',
                'verbose_name_plural': 'Информация о пользователе',
            },
        ),
    ]