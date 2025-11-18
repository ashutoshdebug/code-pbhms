from django.db import models
from django.utils import timezone
from decimal import Decimal
from guests.models import CheckIn, CheckOut

class Billing(models.Model):
    check_out = models.OneToOneField(CheckOut, on_delete=models.CASCADE, related_name='bill', null=True, blank=True)
    check_in = models.ForeignKey(CheckIn, on_delete=models.CASCADE, related_name='bills')

    room_bill = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    room_service = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    bottles = models.DecimalField(max_digits=10, decimal_places=2)
    in_room_facilities = models.DecimalField(max_digits=10, decimal_places=2)
    miscellaneous = models.DecimalField(max_digits=10, decimal_places=2)

    total = models.DecimalField(max_digits=12, decimal_places=2, default=0, editable=False)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Validate first
        if not self.check_out:
            raise ValueError("Cannot create a bill without a checkout record.")
        if self.check_out.check_in != self.check_in:
            raise ValueError("Check In and Check Out must belong to the same guest.")

        # Room rates
        room_rates = {
            'ER': 5000,
            'DR': 2500,
            'NR-(AC)': 1500,
            'NR-(WAC)': 1000,
        }

        # Compute room bill
        room_rate = room_rates.get(self.check_in.room_type, 0)
        self.room_bill = Decimal(room_rate) * Decimal(self.check_out.no_of_days)

        # Compute total
        self.total = (
            self.room_service +
            self.food +
            self.bottles +
            self.in_room_facilities +
            self.miscellaneous +
            self.room_bill
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return  f"Rs.{self.total}"
