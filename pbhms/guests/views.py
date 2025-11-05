from django.shortcuts import render

# Create your views here.
def guests(request):
    return render(request, 'guests.html')

def checkin(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Guest checked in successfully!")
            return redirect('guests:checkin')  # reload form after submission
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CheckInForm()

    return render(request, 'guesthandling/checkin.html', {'form': form})

def checkout(request):
    return render(request, 'guesthandling/checkout.html')