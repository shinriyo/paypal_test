from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse 
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render_to_response
# Create your views here.

def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10.00",
        #"amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        #"notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "notify_url": reverse('paypal-ipn'),
        #"return_url": "https://www.example.com/your-return-location/",
        "return_url": reverse('return-location'),
        #"cancel_return": "https://www.example.com/your-cancel-location/",
        "cancel_return": reverse('cancel-location'),

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("payment.html", context)
