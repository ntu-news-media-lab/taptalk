# Generated by Django 3.0.3 on 2020-03-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('picture_src', models.URLField(null=True)),
                ('saved_articles', models.ManyToManyField(to='articles.Article')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.User')),
                ('is_verified', models.BooleanField(default=False)),
                ('expert_title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Expert',
                'verbose_name_plural': 'Experts',
            },
            bases=('users.user',),
        ),
    ]
