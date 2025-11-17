from django import forms
from django.utils import timezone
from .models import CheckIn

class checkin_form(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = "__all__"
        widgets = {
            'room_type': forms.Select(attrs={'class': "bg-black text-white rounded"}),
            'name': forms.TextInput(attrs={'placeholder': "Enter the name of the Guest", 'class': 'w-[100%] focus:outline-none rounded p-1'}),
            'date': forms.DateTimeInput(attrs={'value': timezone.now().strftime('%Y-%m-%d %H:%M:%S'), 'readonly': 'readonly', 'class': 'focus:outline-none rounded p-1'}),
            'aadhaar_card': forms.TextInput(attrs={'placeholder': "Enter the Aadhaar Card number of the Guest", 'class': 'w-[100%] focus:outline-none rounded p-1', 'minlength':12}),
            'mobile': forms.TextInput(attrs={'placeholder': "Enter the mobile number of the Guest", 'class': 'w-[100%] focus:outline-none rounded p-1', 'minlength':10}),
            'alloted_room': forms.TextInput(attrs={'placeholder': 'Enter the alloted room number of the Guest', 'class': 'w-[100%] focus:outline-none rounded p-1', 'minlength':3})
            
        }


# class checkout_form(forms.Form):
#     checkout_form = forms.CharField(label = "Your name", max_length=100, required=False)