from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact-us', views.contact),
    url(r'^about-us', views.about),
    url(r'^events/$', views.events),
    url(r'^events/(?P<pk>\d+)/$', views.events_detail),
    url(r'^causes/(?P<pk>\d+)/$', views.cause_detail)
]
