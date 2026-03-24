from django.db import models

# Create your models here.

class CustomerModel(models.Model):
    customerName = models.CharField(max_length=150)
    phoneNumber = models.IntegerField()
    address = models.CharField(max_length=500)
    emailAddress = models.EmailField()
    customerType = models.CharField(max_length=150)
    def __str__(self):
        return self.customerName

