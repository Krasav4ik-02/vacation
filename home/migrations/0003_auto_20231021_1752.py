# Generated by Django 3.2.19 on 2023-10-21 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_leaverequest_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavebalance',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='timeentry',
            name='employee',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='LeaveBalance',
        ),
        migrations.DeleteModel(
            name='LeaveRequest',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='TimeEntry',
        ),
    ]
