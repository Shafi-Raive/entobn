# Generated by Django 2.1 on 2019-10-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='englishwords',
            name='Bn_Word',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='englishwords',
            name='En_Word',
            field=models.TextField(max_length=50),
        ),
    ]
