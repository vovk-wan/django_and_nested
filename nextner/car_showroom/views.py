from django.urls import reverse
from django.forms.models import inlineformset_factory
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
# reverse

from nested_formset import nestedformset_factory

from car_showroom import models


class ListCarShowroomsView(ListView):

    model = models.CarShowRoomModel
    fields = '__all__'


class CreateCarShowroomView(CreateView):

    model = models.CarShowRoomModel
    fields = '__all__'

    def get_success_url(self):

        return reverse('car_showrooms-list')


class EditCarsView(UpdateView):

    model = models.CarShowRoomModel
    fields = '__all__'

    def get_template_names(self):

        return ['car_showroom/carmodel_form.html']

    def get_form_class(self):

        return nestedformset_factory(
            models.CarShowRoomModel,
            models.CarModel,
            nested_formset=inlineformset_factory(
                models.CarModel,
                models.CarSpecificationModel,
                fields='__all__'
            )
        )

    def get_success_url(self):

        return reverse('car_showrooms-list')
