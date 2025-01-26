from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=200)
    preview = models.ImageField(upload_to="course_previews", null=True, blank=True)
    description = models.TextField()
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_owned", default=1
    )

    objects = models.Manager()


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to="lesson_previews", null=True, blank=True)
    video_link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lessons_owned", default=1
    )

    objects = models.Manager()
