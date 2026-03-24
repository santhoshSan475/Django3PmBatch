from django.db import models

# Create your models here.

class studentModel(models.Model):
    studentName = models.CharField(max_length=150)
    admissionNo = models.IntegerField()
    standard = models.CharField(max_length=150)
    BloodGroup = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.studentName