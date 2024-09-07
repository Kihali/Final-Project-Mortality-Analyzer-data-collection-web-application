from django.db import models

class ChildMortality(models.Model):
    year = models.IntegerField()
    mortality_rate = models.FloatField()

    def __str__(self):
        return f"{self.year} - {self.mortality_rate}"
