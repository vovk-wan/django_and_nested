from django.contrib import admin


from django.contrib import admin
import nested_admin

from car_showroom.models import CarShowRoomModel
from car_showroom.models import CarModel, CarSpecificationModel


class CarSpecificationInline(nested_admin.NestedStackedInline):
    model = CarSpecificationModel
    sortable_field_name = "power"


class CarInline(nested_admin.NestedStackedInline):
    model = CarModel
    inlines = [CarSpecificationInline]


class CarShowRoomAdmin(nested_admin.NestedModelAdmin):
    inlines = [CarInline]


class CarAdmin(nested_admin.NestedModelAdmin):
    inlines = [CarSpecificationInline]


admin.site.register(CarShowRoomModel, CarShowRoomAdmin)
admin.site.register(CarModel, CarAdmin)
