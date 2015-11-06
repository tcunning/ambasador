from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from referral import views


# http://localhost:8000/referral/test2/
# http://localhost:8000/referral
urlpatterns = [
    url(r'^referral/$', views.referral_list),
    #url(r'^referral/(?P<pk>[0-9]+)/$', views.referral_detail),
    url(r'^referral/(?P<theName>[0-9A-Za-z%_.]+)/$', views.referral_detail),
]

# Allow support for (.json or .api)
#   http://localhost:8000/referral.json
#   http://localhost:8000/referral.api
#
# AND support for Accept headers
#   Accept:application/json     <== JSON View
#   Accept:text/html            <== API View
#
# And support Content-Type Requests
#   --json
#   --form
#
urlpatterns = format_suffix_patterns(urlpatterns)
