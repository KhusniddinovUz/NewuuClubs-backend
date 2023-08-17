from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    group_number = models.CharField(max_length=15, blank=True, null=True)
    student_id = models.CharField(max_length=20, blank=True, null=True)
    student_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email
