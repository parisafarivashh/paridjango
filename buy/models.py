from django.db import models

class Buy(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField()
  stock = models.IntegerField()
  image = models.ImageField(upload_to='image/')

def __str__(self):
  return self.name  

class Register(models.Model):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.IntegerField()

def __str__(self):
  return self.username   
