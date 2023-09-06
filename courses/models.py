from django.db import models
import uuid


class CourseStatus(models.TextChoices):
    not_started = "not started"
    in_progress = "in progress"
    finished = "finished"


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, choices=CourseStatus.choices, default=CourseStatus.not_started
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey(
        "accounts.Account", on_delete=models.PROTECT, related_name="courses", null=True
    )
