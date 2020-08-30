from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Order

def contact(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            listing_id = request.POST['listing_id']
            listing_name = request.POST['listing_name']
            client_id = request.user.id
            client = get_object_or_404(User, id = client_id)
            client_email = client.email
            client_name = client.username

            has_contacted = Order.objects.all().filter(listing_id = listing_id, client_name = client_name)
            if has_contacted:
                return redirect('/listings/'+ listing_id)
            order = Order(listing_id = listing_id, listing_name = listing_name, client_email=client_email, client_name=client_name)
            order.save()
            return redirect('dashboard')
        
        else:
            return redirect('index')

    else:
        return redirect('listings')