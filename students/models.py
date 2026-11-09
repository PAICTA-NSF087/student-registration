from django.db import models


class Student(models.Model):
    student_number =models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.student_number} - {self.first_name} {self.last_name}"