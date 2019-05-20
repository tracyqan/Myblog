# Generated by Django 2.1.5 on 2019-04-29 17:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usercount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='访问时间')),
                ('url', models.CharField(max_length=256, verbose_name='访问的页面')),
                ('user_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usercount.UserIp', verbose_name='IP地址')),
            ],
            options={
                'verbose_name': '访问记录详情',
                'verbose_name_plural': '访问记录详情',
            },
        ),
        migrations.RemoveField(
            model_name='requestdate',
            name='user_ip',
        ),
        migrations.DeleteModel(
            name='RequestDate',
        ),
    ]
