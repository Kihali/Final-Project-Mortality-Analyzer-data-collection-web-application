from django.db import models

class ChildMortality(models.Model):
    facility_name = models.CharField(max_length=255, null=True, blank=True)  
    facility_location = models.CharField(max_length=255, null=True, blank=True)  
    facility_capacity = models.IntegerField(default=0)  
    child_age = models.IntegerField(default=0)  
    child_gender = models.CharField(max_length=10, default="Unknown")  
    cause_of_death = models.CharField(max_length=255, default="Unknown")  
    region_name = models.CharField(max_length=255, null=True, blank=True)  
    population = models.IntegerField(default=0)  
    gdp = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  

    def __str__(self):
        return f"{self.facility_name} - {self.child_age}"
