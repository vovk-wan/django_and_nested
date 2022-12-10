"""Классы для отображения таблиц в Django-admin"""
import nested_admin
from django.contrib import admin

from car_showroom.models import (
    CarModel,
    CarShowRoomModel,
    CarSpecificationModel
)


class CarSpecificationInline(nested_admin.NestedStackedInline):
    """Inline форма для модели CarSpecificationModel"""

    model = CarSpecificationModel
    sortable_field_name = "power"


class CarInline(nested_admin.NestedStackedInline):
    """Inline форма для модели CarModel"""

    model = CarModel
    inlines = [CarSpecificationInline]


class CarShowRoomAdmin(nested_admin.NestedModelAdmin):
    """Форма для модели CarShowRoomModel"""

    inlines = [CarInline]


class CarAdmin(nested_admin.NestedModelAdmin):
    """Форма для модели CarModel"""

    inlines = [CarSpecificationInline]


admin.site.register(CarShowRoomModel, CarShowRoomAdmin)
admin.site.register(CarModel, CarAdmin)
