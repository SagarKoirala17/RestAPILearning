from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.TextField()
    customer_id=models.IntegerField()


    def __str__(self):
        return self.first_name