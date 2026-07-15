from django.db import models

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    age = models.IntegerField(blank=False,null=False)
    breed = models.CharField(max_length=100,blank=False,null=False)

    def __str__(self):
        return self.name