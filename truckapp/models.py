from django.db import models


class Truck(models.Model):
    truck_name = models.CharField(max_length=100)
    truck_location = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100, null=True)
    geo_location = models.CharField(max_length=100, null=True)
    truck_opening_time=models.CharField(max_length=20,null=True)
    truck_closing_time=models.CharField(max_length=20,null=True)


    def __str__(self):
        return self.truck_name
