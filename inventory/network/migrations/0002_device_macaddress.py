# Generated by Django 3.1.4 on 2020-12-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='macaddress',
            field=models.CharField(default='unknown', max_length=20),
            preserve_default=False,
        ),
    ]
