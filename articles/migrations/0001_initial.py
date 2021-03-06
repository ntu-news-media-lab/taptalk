# Generated by Django 3.0.3 on 2020-03-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('byline', models.TextField(blank=True, null=True)),
                ('num_views', models.IntegerField(blank=True, default=0)),
                ('num_shares', models.IntegerField(blank=True, default=0)),
                ('picture_src', models.URLField(blank=True, null=True)),
                ('headline', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('date_published', models.DateTimeField()),
                ('sections', models.ManyToManyField(related_name='article', to='sections.Section')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
