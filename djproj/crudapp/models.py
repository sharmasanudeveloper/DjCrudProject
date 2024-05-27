from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=80)
    address = models.CharField(max_length=150,null=False)
    department = models.CharField(max_length=20,default=True)
    
    def __str__(self):
        return str(self.id)
