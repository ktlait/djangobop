# Generated by Django 2.0.2 on 2018-07-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choose', '0006_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colour',
            name='rgb',
            field=models.CharField(max_length=15),
        ),
    ]
