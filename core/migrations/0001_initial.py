import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=225)),
                ('email', models.TextField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('age_limit', models.CharField(choices=[
                 ('All', 'All'), ('Kids', 'Kids')], max_length=10)),
                ('subscriptions', models.FileField(upload_to='Channel'))
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('decription', models.TextField(
                    blank=True, max_length=225, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('videos', models.FileField(upload_to='Video')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('descripion', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[
                 ('sports', 'Sports'),
                 ('gaming', 'Gaming'),
                    ('live', 'Live'),
                    ('premium', 'Premium'),
                    ('fashion', 'Fashion'),
                    ('beauty', 'Beauty'),
                    ('learning', 'Learning'),
                    ('movies', 'Movies'),
                    ('shows', 'Shows'),
                    ('news', 'News'),
                    ('other', 'Other')], max_length=10)),
                ('age_limit', models.CharField(choices=[
                 ('All', 'All'), ('Kids', 'Kids')], max_length=10)),
                ('videos', models.ManyToManyField(to='core.Video')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                 max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True,
                 max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True,
                 max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True,
                 max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                 verbose_name='staff status')),
                ('date_joined', models.DateTimeField(
                    default=django.utils.timezone.now, verbose_name='date joined')),
                ('profiles', models.ManyToManyField(
                    blank=True, to='core.Profile')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
