from django.db import models

# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=4, null=True)

    def __str__(self):
        return f"{self.name}({self.code})"

class Student(models.Model):
    last = models.CharField(max_length = 20)
    first = models.CharField(max_length = 20)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name="students")
