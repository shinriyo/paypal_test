from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	# ipn
	(r'^something/paypal/', include('paypal.standard.ipn.urls')),
	url(r'^money/', 'blogs.views.view_that_asks_for_money', name='return-location'),
	# pdt
    #(r'^paypal/pdt/', include('paypal.standard.pdt.urls')),
	#url(r'^money/', 'paypal.standard.pdt.views.pdt', name='return-location'),
	
	# url(r'^return-location/', 'blogs.views.view_that_asks_for_money', name='return-location'),
	# url(r'^cancel-location/', 'blogs.views.view_that_asks_for_money', name='cancel-location'),
)
