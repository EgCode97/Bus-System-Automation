from django.contrib import admin
from .models import BusStop, BusUnit, Route, Zone
# Register your models here.

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zone')

class BusUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'location')


class RouteAdmin(admin.ModelAdmin):
    list_display = ('route',)

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(BusStop, BusStopAdmin)
admin.site.register(BusUnit, BusUnitAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Zone, ZoneAdmin)