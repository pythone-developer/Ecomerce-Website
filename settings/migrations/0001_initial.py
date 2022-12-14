# Generated by Django 4.1.3 on 2022-12-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='company', verbose_name='Logo')),
                ('subtitle', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Subtitle')),
                ('fb_link', models.URLField(blank=True, null=True, verbose_name='FacebookLink')),
                ('tw_link', models.URLField(blank=True, null=True, verbose_name='TwaterLink')),
                ('li_link', models.URLField(blank=True, null=True, verbose_name='LinkedinLink')),
                ('adress', models.TextField(max_length=200, verbose_name='Adress')),
                ('phone_number', models.TextField(max_length=200, verbose_name='PhoneNumber')),
                ('email', models.TextField(max_length=200, verbose_name='Email')),
                ('call_us', models.CharField(max_length=50, verbose_name='CallUs')),
                ('email_us', models.EmailField(max_length=254, verbose_name='EmailUS')),
            ],
        ),
    ]
