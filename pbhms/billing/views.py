from django.shortcuts import render
from .forms import billing_form
from guests.models import CheckOut

# Create your views here.
def billing(request):
    guest = None
    aadhaar_search = request.GET.get("aadhaar_search")
    if aadhaar_search:
        try:
            guest = CheckOut.objects.get(check_in__aadhaar_card = aadhaar_search)
        except CheckOut.DoesNotExist:
            guest = None
    if request.method == "POST":
        form = billing_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = billing_form()
    return render(request, 'billing.html', {'form': form, 'guest': guest})