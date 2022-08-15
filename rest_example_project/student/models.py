from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default = 0)
    class_student = models.CharField(max_length=20)
    height = models.FloatField(default=0)
    weight = models.FloatField(default = 0)

    def __str__(self):
        return self.name
    