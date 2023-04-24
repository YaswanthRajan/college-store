from django.db import models


# Create your models here.
class bio(models.Model):
    name = models.CharField(max_length=35,null=True)
    DOB = models.DateField(null=True)
    Age = models.IntegerField(null=True)
    Gender = models.TextField(null=True)
    phone = models.IntegerField(null=True)
    email = models.TextField(null=True)
    address = models.TextField(null=True)
    department = models.TextField(null=True)
    material = models.TextField(null=True)
