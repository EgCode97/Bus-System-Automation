from django.contrib import admin
from .models import BusStop, BusUnit, Route
# Register your models here.

class BusStopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

class BusUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'location')


class RouteAdmin(admin.ModelAdmin):
    list_display = ('route',)


admin.site.register(BusStop, BusStopAdmin)
admin.site.register(BusUnit, BusUnitAdmin)
admin.site.register(Route, RouteAdmin)