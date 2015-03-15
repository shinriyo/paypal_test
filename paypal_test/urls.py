from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paypal_test.views.home', name='home'),
    url(r'', include('blogs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
# from paypal.standard.ipn.signals import payment_was_successful
from blogs.models import PurchaseHistory


def show_me_the_money(sender, **kwargs):
    print 'show_me_the_money called'
    p = PurchaseHistory(name='test')
    p.save()

    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        print 'payment_status is ST_PP_COMPLETED'
        # Undertake some action depending upon `ipn_obj`.
        p = PurchaseHistory(name='ST_PP_COMPLETED')
        p.save()
        #if ipn_obj.custom == "Upgrade all users!":
        #    Users.objects.update(paid=True)
    #else:
    #    #...

# valid_ipn_received.connect(show_me_the_money)
payment_was_successful.connect(show_me_the_money)
# DeprecationWarning: payment_was_successful is deprecated, please migrate to valid_ipn_received instead
# payment_was_successful.connect(show_me_the_money)
