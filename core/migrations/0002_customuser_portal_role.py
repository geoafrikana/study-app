# Generated by Django 4.2.2 on 2023-07-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='portal_role',
            field=models.CharField(choices=[('ins', 'Instructor'), ('stu', 'Student')], default='stu', max_length=15),
        ),
    ]