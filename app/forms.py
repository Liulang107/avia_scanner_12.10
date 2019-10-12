from django import forms
from django.forms import SelectDateWidget

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    # Добавьте здесь поля, описанные в задании
    MONTH_CHOICES = {
        1: ('Январь'), 2: ('Февраль'), 3: ('Март'), 4: ('Аперль'),
        5: ('Май'), 6: ('Июнь'), 7: ('Июль'), 8: ('Август'),
        9: ('Сентябрь'), 10: ('Октябрь'), 11: ('Ноябрь'), 12: ('Декабрь')
    }

    city_from = forms.CharField(label='Город отправления', widget=AjaxInputWidget(
        url='api/city_ajax',
        attrs={'class': 'inline right-margin'}))
    city_to = forms.ModelChoiceField(label='Город прибытия', queryset=City.objects.all())
    flight_date = forms.DateField(label='Дата', widget=SelectDateWidget(months=MONTH_CHOICES))
