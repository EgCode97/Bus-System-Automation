from django.db import models

# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150, help_text='Alcance y ubicacion de la zona')

    def __str__(self):
        return self.name

class BusStop(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True, unique=True)
    address = models.CharField(max_length=150)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=150, verbose_name='Route Name', unique=True)
    route_description = models.CharField(max_length=150, verbose_name='Route description', default="No disponible")
    stop1 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name="Parada1", verbose_name='Parada 1')
    stop2 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada2", verbose_name='Parada 2')
    stop3 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada3", verbose_name='Parada 3')
    stop4 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada4", verbose_name='Parada 4')
    stop5 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada5", verbose_name='Parada 5')
    stop6 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada6", verbose_name='Parada 6')
    stop7 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada7", verbose_name='Parada 7')
    stop8 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada8", verbose_name='Parada 8')
    stop9 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada9", verbose_name='Parada 9')
    stop10 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada10", verbose_name='Parada 10')
    stop11 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada11", verbose_name='Parada 11')
    stop11 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada12", verbose_name='Parada 12')
    stop13 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada13", verbose_name='Parada 13')
    stop14 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada14", verbose_name='Parada 14')
    stop15 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada15", verbose_name='Parada 15')
    stop16 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada16", verbose_name='Parada 16')
    stop17 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada17", verbose_name='Parada 17')
    stop18 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada18", verbose_name='Parada 18')
    stop19 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada19", verbose_name='Parada 19')
    stop20 = models.ForeignKey(BusStop, on_delete=models.SET_NULL, null=True, blank=True, related_name= "Parada20", verbose_name='Parada 20')

    def __str__(self):
        return self.name


class BusUnit(models.Model):
    id = models.IntegerField(verbose_name='ID number:', unique=True, primary_key=True)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    location = models.ForeignKey(BusStop, on_delete=models.CASCADE)
