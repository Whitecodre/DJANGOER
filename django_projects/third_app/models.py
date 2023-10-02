from django.db import models
from django.utils import timezone

# Create your models here.

class practice(models.Model):
    Name = models.TextField(max_length=20)
    Age = models.IntegerField()


class customer_data(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    Firstname = models.TextField()
    Lastname = models.TextField()
    Email_Address = models.EmailField()
    Phone_Number = models.IntegerField()
    Age = models.IntegerField()
    DOB = models.DateTimeField()
    Nationality = models.TextField()
    State_Of_Origin = models.TextField()


class apis(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    Name = models.TextField()
    Department = models.TextField()