# Generated by Django 4.1.7 on 2023-03-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_remove_student_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='gpa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
