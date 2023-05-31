from django.db import models

# Create your models here.

class album(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    price = models.IntegerField()
    pic = models.ImageField(upload_to='pic')
    disc = models.TextField()


    def __str__(self):
        return self.name
