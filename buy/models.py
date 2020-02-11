from django.db import models

class Buy(models.Model):
  name = models.CharField(max_length=100)
  price = models.FloatField()
  stock = models.IntegerField()
  image = models.ImageField(upload_to='image/')

def __str__(self):
  return self.name  