# Generated by Django 3.0.3 on 2020-03-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(),
        ),
    ]
