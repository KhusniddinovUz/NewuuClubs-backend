from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField()
    logo = models.ImageField(upload_to="logos/")
    students_count = models.IntegerField()

    def __str__(self):
        return self.title
