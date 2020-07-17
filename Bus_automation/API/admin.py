from django.contrib import admin
from .models import BusStop, BusUnit, Route, Zone
# Register your models here.

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zone')

class BusUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'location')


class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'route_description',
    'stop1', 'stop2', 'stop3', 'stop4', 'stop5',
    'stop6', 'stop7', 'stop8', 'stop9', 'stop10',
    'stop11', 'stop11', 'stop13', 'stop14', 'stop15',
    'stop16', 'stop17', 'stop18', 'stop19', 'stop20',)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(BusStop, BusStopAdmin)
admin.site.register(BusUnit, BusUnitAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Zone, ZoneAdmin)