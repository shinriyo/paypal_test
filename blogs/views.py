from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse 
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def view_that_asks_for_money(request):
    url = "http://47cc7e44.ngrok.com"
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10.00",
        #"amount": "10000000.00",
        "item_name": "name of the item",
        #"invoice": "unique-invoice-id",
        "invoice": "unique-invoice-id12",
        #"notify_url": "https://www.example.com" + reverse('paypal-ipn'),
        "notify_url": url + reverse('paypal-ipn'),
        #"return_url": "https://www.example.com/your-return-location/",
        "return_url": url + reverse('return-location'),
        #"cancel_return": "https://www.example.com/your-cancel-location/",
        #"cancel_return": reverse('cancel-location'),
        "cancel_return": url + reverse('return-location'),

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render_to_response("payment.html", context)
