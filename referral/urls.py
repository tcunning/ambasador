from django.conf.urls import url
from referral import views


# http://localhost:8000/referral/test2/
# http://localhost:8000/referral
urlpatterns = [
    url(r'^referral/$', views.referral_list),
    #url(r'^referral/(?P<pk>[0-9]+)/$', views.referral_detail),
    url(r'^referral/(?P<theName>[0-9A-Za-z%_.]+)/$', views.referral_detail),
]
  
