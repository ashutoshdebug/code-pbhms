from django.contrib import admin
from .models import Billing

class Guest_Billing(admin.ModelAdmin):
    list_display = ('check_in', 'check_out', 'room_bill', 'room_service', 'food', 'bottles', 'in_room_facilities', 'miscellaneous', 'date', 'total')
    search_fields = ('check_in__name', 'check_in__aadhaar_card')
    list_filter = ('date',)
    readonly_fields = ('room_bill', 'total')

admin.site.register(Billing, Guest_Billing)