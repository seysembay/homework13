from django.db import models


class Course(models.Model):
    class Meta:
        verbose_name_plural = "Courses"

    name = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
