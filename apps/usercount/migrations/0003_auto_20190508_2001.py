# Generated by Django 2.1.5 on 2019-05-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercount', '0002_auto_20190429_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdetail',
            name='ip_place',
            field=models.CharField(default='无', max_length=30, verbose_name='IP归属地'),
        ),
        migrations.AddField(
            model_name='userip',
            name='ip_place',
            field=models.CharField(default='无', max_length=30, verbose_name='IP归属地'),
        ),
    ]