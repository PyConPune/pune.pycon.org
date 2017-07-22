# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.core.validators
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, max_length=30, verbose_name='username', unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', verbose_name='groups', related_query_name='user', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', related_query_name='user', blank=True, to='auth.Permission')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2018)),
                ('first_name', models.CharField(verbose_name='first name', max_length=255)),
                ('last_name', models.CharField(verbose_name='last name', null=True, blank=True, max_length=255)),
                ('contact', models.CharField(verbose_name='contact', null=True, blank=True, max_length=15)),
                ('location', models.CharField(verbose_name='location', null=True, blank=True, max_length=255)),
                ('age_group', models.CharField(verbose_name='age group', null=True, blank=True, max_length=255)),
                ('gender', models.CharField(verbose_name='gender', null=True, choices=[('1', 'Less than 10'), ('2', '11-17'), ('3', '18-24'), ('4', '25-34'), ('5', '35-44'), ('6', '45 and over')], blank=True, max_length=255)),
                ('occupation', models.CharField(verbose_name='occupation', null=True, choices=[('W', 'Working Professional'), ('S', 'Student'), ('U', 'Temporarily Unemployed'), ('C', 'Carer'), ('R', 'Retired')], blank=True, max_length=1)),
                ('company', models.CharField(verbose_name='company', null=True, blank=True, max_length=255)),
                ('company_title', models.CharField(verbose_name='company title', null=True, blank=True, max_length=255)),
                ('website', models.URLField(null=True, blank=True)),
                ('subscribed', models.BooleanField(verbose_name='subscribed', max_length=255, default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
