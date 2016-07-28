from django import forms
from django.forms import ModelForm
from .models import Customer
from django_select2.forms import ModelSelect2Widget


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['customer']

    customer = forms.ModelChoiceField(
        widget=ModelSelect2Widget(
            attrs={'class': 'form-control', 'data-placeholder': 'Выберите заказчика...'},
            model=Customer,
            search_fields=['customer__istartswith'],
        ),
        label='Заказчик',
        required=False,
        queryset=Customer.objects.all(),
    )
    # customer = forms.ModelChoiceField(queryset=Customer.objects.all(),
    #                                   empty_label='Выберите заказчика...',
    #                                   widget=forms.Select(attrs={'class': 'form-control'}),
    #                                   label='Заказчик')
