from django.db import models

# Create your models here.
class HighBlood(models.Model):
    username=models.CharField(max_length=40)
    sex=models.CharField(max_length=10,default="男")
    tall=models.DecimalField(max_digits=6,decimal_places=2)
    weight=models.DecimalField(max_digits=6,decimal_places=2)
    smoke=models.CharField(max_length=10,default="不吸")
    drink=models.CharField(max_length=10,default="不喝酒")