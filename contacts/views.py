from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_name = request.POST['realtor_name']

        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request, ' כבר הגשת הצעה על הנכס זה')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing,
                          listing_id=listing_id,
                          name=name,
                          email=email,
                          phone=phone,
                          message=message,
                          user_id=user_id)

        contact.save()

        messages.success(request, 'ההודעה נשלחה בהצלחהת נחזור אליך בהקדם')
        return redirect('/listings/' + listing_id)
