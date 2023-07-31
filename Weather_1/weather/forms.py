from .models import City
from django.forms import ModelForm, TextInput, widgets


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        # атрибуты по которым я буду обращаться для выводов информации из сайта( для csrf)
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город',
        })}

