from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Bank(models.Model):
    
    name = models.CharField(max_length=20)
    id = models.BigIntegerField(primary_key=True)
    def __str__(self):
        return str(self.id)

class Public_branches(models.Model):
    ifsc = models.CharField(max_length=11,primary_key=True)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    
    def __str__(self):
        return str(self.ifsc)

class Public_bank_branches(models.Model):
    
    ifsc = models.CharField(max_length=11)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)
    
    def __str__(self):
        return str(self.ifsc)
