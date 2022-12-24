from django_filters import widgets, FilterSet, DateFilter
from django import forms
from .models import *


class NewsFilter(FilterSet):
    data_pub = DateFilter(
        field_name='data_pub',
        label='Опубликовано с:',
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'DD/MM/YYYY'
            }
        ),
    )

    class Meta:
       #
       model = News
       fields = {
           'title': ['icontains'],
           'author': ['exact'],
       }