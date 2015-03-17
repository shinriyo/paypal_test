# paypal_test

valid_ipn_received.connect(show_me_the_money) can't catch.

# show_me_the_money() never is called in `paypaltest/urls.py`

I resolved it!!
You must set of your PayPal site.

```
the print functions doesn't work.
print 'show_me_the_money called'
print 'payment_status is ST_PP_COMPLETED'
```

## PayPal sandbox

ID: shinriyotest@gmail.com

PASS: testtest

## Admin

ID: shinriyotest

PASS: testtest


## Information

Django 1.6.4
django-paypal 0.2

You also install for watching your admin.

```
pip install pytz
```

PayPal is IPN
IPN is this.
http://django-paypal.readthedocs.org/en/latest/standard/ipn.html

