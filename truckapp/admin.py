from django.contrib import admin
from truckapp.models import Truck
class TruckAdmin(admin.ModelAdmin):
        list_display=['truck_name','truck_location','truck_opening_time','truck_closing_time']
admin.site.register(Truck,TruckAdmin)

