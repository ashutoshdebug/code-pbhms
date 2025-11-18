from django.db import models
from django.utils import timezone

# Create your models here.

class CheckIn(models.Model):
    room_Types = [
        ('ER', 'Executive Rooms'),
        ('DR', 'Deluxe Rooms'),
        ('NR-(AC)', 'Normal Rooms (AC)'),
        ('NR-(WAC)', 'Normal Rooms (Without AC)'),
    ]

    room_type = models.CharField(max_length = 50, choices = room_Types)
    date = models.DateTimeField(default = timezone.now)
    name = models.CharField(max_length = 100, null = False)
    aadhaar_card = models.CharField(null = False, max_length = 12, unique= True)
    mobile = models.CharField(max_length = 10, null= True)
    alloted_room = models.CharField(max_length = 3, null = False)

    def __str__(self):
        return self.name
    
# One to One field CHECKOUT
class CheckOut(models.Model):
    check_in = models.OneToOneField(CheckIn, on_delete = models.CASCADE, related_name = 'checkout')
    checkout_date = models.DateTimeField(default = timezone.now)
    no_of_days = models.PositiveIntegerField(editable=False)

    # total = models.OneToOneField(Billing, on_delete = models.CASCADE, default = 0)
    def save(self, *args, **kwargs):
        checkin_date = self.check_in.date
        checkout_date = self.checkout_date

        # difference in date
        delta_days = (checkout_date.date() - checkin_date.date()).days

        # Ensure minimum 1 day
        self.no_of_days = max(delta_days, 1)

        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.check_in.name
    
    @property
    def total_amount(self):
        bill = getattr(self, 'bill', None)
        return bill.total if bill else 0