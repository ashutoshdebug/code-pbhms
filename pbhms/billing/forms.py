from django import forms
from django.utils import timezone
from .models import Billing

class billing_form(forms.ModelForm):
    class Meta:
        model = Billing
        fields = "__all__"
        widgets = {
            'check_in': forms.Select(attrs={'class': 'bg-black w-full focus:outline-none'}),
            'check_out': forms.Select(attrs={'class': 'bg-black w-full focus:outline-none'}),
            'room_service': forms.TextInput(attrs={'placeholder': 'Enter total bill of Room service if taken', 'class': 'w-full focus:outline-none'}),
            'food': forms.TextInput(attrs={'placeholder': 'Enter total food bill if ordered', 'class': 'w-full focus:outline-none'}),
            'room_bill': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'w-full focus:outline-none'}),
            'bottles': forms.TextInput(attrs={'placeholder': 'Enter the water bill if taken', 'class': 'w-full focus:outline-none'}),
            'in_room_facilities': forms.TextInput(attrs={'placeholder': 'Enter the bill for room facilities', 'class': 'w-full focus:outline-none'}),
            'total': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'w-full focus:outline-none'}),
            'miscellaneous': forms.TextInput(attrs={'placeholder': 'Enter any miscellaneous bill', 'class': 'w-full focus:outline-none'}),
            'date': forms.DateTimeInput(attrs={'value': timezone.now().strftime('%Y-%m-%d %H:%M:%S'), 'class': 'focus:outline-none' ,'readonly': 'readonly', 'class': 'w-full'})
        }