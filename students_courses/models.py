from django.db import models
import uuid


class StudentCourseStatus(models.TextChoices):
    pending = "pending"
    accepted = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(
        max_length=8,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.pending,
    )
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="students_courses"
    )
    student = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="students_courses"
    )
