from django.db import models
from car_list.models import Category

# Create your models here.
class Car(models.Model):
    brand = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_post/media/uploads/',blank=True,null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name