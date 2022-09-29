from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    salary=models.FloatField()
    dob=models.DateField()
    class Meta:
        db_table='employee'
