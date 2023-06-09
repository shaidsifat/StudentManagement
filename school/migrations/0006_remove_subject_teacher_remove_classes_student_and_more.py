# Generated by Django 4.1.7 on 2023-03-13 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_teacher_subject_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='student',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='subjects',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
        migrations.AddField(
            model_name='classes',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.student'),
        ),
        migrations.AddField(
            model_name='classes',
            name='subjects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.subject'),
        ),
    ]
