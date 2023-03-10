# Generated by Django 4.1.7 on 2023-03-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0003_rename_deadline_date_assignment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file',
            field=models.FileField(upload_to='media/assignments/'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(upload_to='media/submissions/'),
        ),
    ]
