from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name