
from django.conf.urls import include, url
from . import views

"""
Definition of urls for teamprediction.
"""

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', teamprediction.views.home, name='home'),
    # url(r'^teamprediction/', include('teamprediction.teamprediction.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^teamselection/$', index),
]
