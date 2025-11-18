from django.shortcuts import render, redirect
from .models import CheckIn, CheckOut
from .forms import checkin_form, checkout_form

# Create your views here.
def guests(request):
    return render(request, 'guests.html')

def checkin(request):
    # return render(request, 'guesthandling/checkin.html') # Direct loading of the page
    guest = None
    aadhaar_search = request.GET.get("aadhaar_search")
    if aadhaar_search:
        try:
            guest = CheckIn.objects.get(aadhaar_card = aadhaar_search)
        except CheckIn.DoesNotExist:
            guest = None

    if request.method == "POST":
        form = checkin_form(request.POST)
        if form.is_valid():
            form.save()
            # room_type = form.cleaned_data['room_type']
            # date = form.cleaned_data['date']
            # name = form.cleaned_data['name']
            # aadhaar_card = form.cleaned_data['aadhaar_card']
            # mobile = form.cleaned_data['mobile']
            # alloted_room = form.cleaned_data['alloted_room']
            return redirect('guests:checkin')

    else:
        form = checkin_form()
    return render(request, 'guesthandling/checkin.html', {'form': form, 'guest': guest,})
        

def checkout(request):
    # return render(request, 'guesthandling/checkout.html')
    guest = None
    aadhaar_search = request.GET.get("aadhaar_search")
    if aadhaar_search:
        try:
            guest = CheckOut.objects.get(check_in__aadhaar_card = aadhaar_search)
        except CheckOut.DoesNotExist:
            guest = None

    if request.method == "POST":
        form1 = checkout_form(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('guests:checkout')
    else:
        form1 = checkout_form()
    return render(request, 'guesthandling/checkout.html', {'form1': form1, 'guest': guest,})
    