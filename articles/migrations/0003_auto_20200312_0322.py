# Generated by Django 3.0.3 on 2020-03-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200312_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='num_sections',
            field=models.IntegerField(null=True),
        ),
    ]