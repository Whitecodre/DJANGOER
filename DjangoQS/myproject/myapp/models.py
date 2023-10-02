from django.db import models

# Create your models here.

class real_model(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.TextField()
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=30)
