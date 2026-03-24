from django.db import models

# Create your models here.


class EmployeeModel(models.Model):
    empName = models.CharField(max_length=150)
    empId = models.IntegerField()
    designation = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phoneNo = models.IntegerField()

    def __str__(self):
        return self.empName
