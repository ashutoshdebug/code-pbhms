from django.contrib import admin
from .models import CheckIn, CheckOut


@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'date', 'name', 'aadhaar_card', 'mobile', 'alloted_room')
    search_fields = ('name', 'aadhaar_card', 'mobile')
    list_filter = ('room_type', 'date')


@admin.register(CheckOut)
class CheckOutAdmin(admin.ModelAdmin):
    list_display = ('check_in', 'checkout_date', 'no_of_days', 'get_total')
    search_fields = ('check_in__name', 'check_in__aadhaar_card')
    list_filter = ('checkout_date',)

    # Make NO OF DAYS visible and non-editable in admin
    readonly_fields = ('no_of_days', 'bill_amount_display')

    # Show these fields in the admin form
    fields = ('check_in', 'checkout_date', 'no_of_days', 'bill_amount_display')

    def get_total(self, obj):
        """Show total amount from related Billing record if available."""
        return f"₹{obj.total_amount:.2f}" if obj.total_amount else "—"
    get_total.short_description = "Total Bill (₹)"

    def bill_amount_display(self, obj):
        """Show bill amount below number of days in form."""
        if obj and hasattr(obj, 'bill'):
            return f"₹{obj.bill.total:.2f}"
        return "—"
    bill_amount_display.short_description = "Bill Amount (₹)"

