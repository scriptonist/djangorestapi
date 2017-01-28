from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField() # at the end of day
    volume = models.IntegerField() # How many times sales was done for the particular stock
    def __str__(self):
        return self.ticker
