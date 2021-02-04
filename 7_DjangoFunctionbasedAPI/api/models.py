from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(null=False, unique=True,
                          auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
