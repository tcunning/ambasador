from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from referral import views


# http://localhost:8000/landing?link=<name> <== Final landing page
# http://localhost:8000/referral            <== API (list and add)
# http://localhost:8000/referral/<name>     <== API (get and modify)
# http://localhost:8000/<name>              <== refer redirect
# http://localhost:8000                     <== Overview page
urlpatterns = [
    url(r'landing/?$', views.landingPage),
    url(r'^referral/$', views.ReferralList.as_view()),
    url(r'^referral/(?P<theName>[0-9A-Za-z%_.]+)/?$', views.ReferralDetail.as_view()),
    url(r'^(?P<theName>[0-9A-Za-z%_.]+)', views.referral_execute),
    url(r'^', views.overviewPage),
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
