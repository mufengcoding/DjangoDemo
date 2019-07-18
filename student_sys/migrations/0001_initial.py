# Generated by Django 2.2.3 on 2019-07-17 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('sex', models.IntegerField(choices=[(1, 'boy'), (2, 'girl'), (0, 'unknow')], verbose_name='sex')),
                ('profession', models.CharField(max_length=128, verbose_name='job')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('qq', models.CharField(max_length=128, verbose_name='QQ')),
                ('phone', models.CharField(max_length=128, verbose_name='phone')),
                ('status', models.IntegerField(choices=[(0, 'apply'), (1, 'pass'), (2, 'refuse')], default=0, verbose_name='check_status')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
            ],
            options={
                'verbose_name': 'student_info',
                'verbose_name_plural': 'student_info',
            },
        ),
    ]