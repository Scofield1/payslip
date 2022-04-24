from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    position = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    hours = models.PositiveIntegerField(default=0)
    grade_status = models.ForeignKey(Grade, on_delete=models.CASCADE)
    gross_salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.gross_salary = (self.grade_status.salary * self.hours)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name


