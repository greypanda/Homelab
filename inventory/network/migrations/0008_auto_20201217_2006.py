# Generated by Django 3.1.4 on 2020-12-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20201216_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='location',
            field=models.CharField(default='Unkknown', max_length=128),
        ),
        migrations.AlterField(
            model_name='device',
            name='osfamily',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='osname',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='ostype',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='osvendor',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='vendor',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
