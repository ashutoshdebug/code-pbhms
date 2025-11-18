from django.shortcuts import render

# Create your views here.
def services(request):
    head = ["Type of Room", "Facilities", "Cost(per day/guest)"]
    roomdata = [
        ['Executive Room', 'Wi-Fi, TV, Air Conditioner, Bathroom with Geyser, Tub and Jacuzzi, Breakfast, Lunch, Dinner', 'Rs.5000'],
        ['Deluxe Room', 'Wi-Fi, TV, Air Conditioner, Bathroom with Tub and Geyser, Lunch, Dinner', 'Rs.2500'],
        ['Normal Room(with AC)', 'Wi-Fi, TV, Air Conditioner, Bathroom with Geyser', 'Rs.1500'],
        ['Normal Room(Non-AC)', 'Wi-Fi, TV, Bathroom with Geyser', 'Rs.1000'],
    ]
    return render(request, "services.html", {
        "head": head,
        "roomdata": roomdata,
    })