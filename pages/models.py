from distutils.command.upload import upload
from unicodedata import category, name
from django.db import models



class Food3(models.Model):
    name = models.CharField(max_length=30)
    cal = models.DecimalField(max_digits = 6, decimal_places=3)
    carb = models.DecimalField(max_digits = 6, decimal_places=3)
    fat = models.DecimalField(max_digits = 6, decimal_places=3)
    prot = models.DecimalField(max_digits = 6, decimal_places=3)
    img = models.ImageField(upload_to = 'foodimgs')

    def __str__(self) :
        return self.name
    
    class Meta :
        ordering= ['name']


class Workout3(models.Model):
    cat = [
        ('arm','arm'),
        ('back','back'),
        ('chest','chest'),
        ('legs','legs'),
        ('shoulder','shoulder'),
    ]
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=20,choices=cat)
    img = models.ImageField(upload_to = 'workimgs')
    def __str__(self) :
        return self.name
    


# Create your models here.
