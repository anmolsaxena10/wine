from django.db import models
#,country,description,designation,points,price,province,region_1,region_2,variety,winery
# Create your models here.
class Wine(models.Model):
    country = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=2000, null=True)
    designation = models.CharField(max_length=200, null=True)
    points = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    province = models.CharField(max_length=200, null=True)
    region_1 = models.CharField(max_length=200, null=True)
    region_2 = models.CharField(max_length=200, null=True)
    variety = models.CharField(max_length=200, null=True)
    winery = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.designation+' '+self.price+' '+self.country