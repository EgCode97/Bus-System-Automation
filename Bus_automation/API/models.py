from django.db import models

# Create your models here.
class BusStop(models.Model):
    address = models.CharField(max_length=150)
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Route(models.Model):
    route = models.CharField(max_length=150, verbose_name='Route Name')

    def __str__(self):
        return self.route

class BusUnit(models.Model):
    id = models.IntegerField(verbose_name='ID number:', unique=True, primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    location = models.ForeignKey(BusStop, on_delete=models.CASCADE)
