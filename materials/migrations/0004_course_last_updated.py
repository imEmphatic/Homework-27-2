# Generated by Django 5.1.5 on 2025-01-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_course_owner_alter_lesson_owner_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
