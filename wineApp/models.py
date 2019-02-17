from django.db import models
#,country,description,designation,points,price,province,region_1,region_2,variety,winery
# Create your models here.
class Wine(models.Model):
    country = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    designation = models.CharField(max_length=200)
    points = models.IntegerField()
    price = models.FloatField()
    province = models.CharField(max_length=200)
    region_1 = models.CharField(max_length=200)
    region_2 = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    winery = models.CharField(max_length=200)

    def __str__(self):
        return self.designation+' '+self.price+' '+self.country