# Generated by Django 2.2.6 on 2019-10-30 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20191030_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookPages',
            field=models.PositiveIntegerField(default=10),
        ),
    ]