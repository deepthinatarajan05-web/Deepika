from django.db import models
class Student(models.Model):
     name=models.CharField(max_length=30)
     age=models.IntegerField()
     course=models.CharField(max_length=30)
def __str__(self):
    return f"{self.name} ({self.course})"
# Create your models here.
