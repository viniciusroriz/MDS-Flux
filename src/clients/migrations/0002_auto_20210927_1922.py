# Generated by Django 3.2.6 on 2021-09-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='number',
            field=models.CharField(max_length=11),
        ),
    ]
