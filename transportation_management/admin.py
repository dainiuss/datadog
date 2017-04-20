from django.contrib import admin
from .models import Vehicle, TravelReport


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'vehicle_name', 'takes_fuel_while_standing', 'takes_fuel_while_moving', 'takes_fuel_while_unloading')
    fields = ('vehicle_name', 'takes_fuel_while_standing', 'takes_fuel_while_moving', 'takes_fuel_while_unloading')
    search_fields = ('vehicle_name',)

    ordering = ('vehicle_name',)


admin.site.register(Vehicle, VehicleAdmin)


class TravelReportAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'vehicle', 'route', 'date', 'time_left_terminal', 'time_arrived_to_client', 'time_left_client',
        'time_back_to_terminal', 'time_unloading', 'speedometer_at_leaving', 'speedometer_at_arrival')
    fields = ('vehicle', 'route', 'date', 'time_left_terminal', 'time_arrived_to_client', 'time_left_client',
              'time_back_to_terminal', 'time_unloading', 'speedometer_at_leaving', 'speedometer_at_arrival')
    search_fields = ('route',)

    ordering = ('-id',)


admin.site.register(TravelReport, TravelReportAdmin)
