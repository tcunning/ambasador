"""
http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
"""
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from referral.models import Referral
from referral.serializers import ReferralSerializer


# http://localhost:8000/referral/
#
class ReferralList(APIView):
    #permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        referral = Referral.objects.all()
        serializer = ReferralSerializer(referral, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReferralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# http://localhost:8000/referral/test/
#
class ReferralDetail(APIView):
    #permission_classes = (permissions.AllowAny,)
    
    def get_object(self, theName):
        try:
            return Referral.objects.get(name=theName)
        except Referral.DoesNotExist:
            raise Http404

    def get(self, request, theName, format=None):
        referral = self.get_object(theName)
        serializer = ReferralSerializer(referral)
        return Response(serializer.data)

    # We only allow the name to be saved via put
    def put(self, request, theName, format=None):
        try:
            referral = self.get_object(theName)
            referral.name = request.data["name"]
            referral.count = int(request.data["count"])
            referral.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValueError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, theName, format=None):
        referral = self.get_object(theName)
        referral.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# http://localhost:8000/referral/test/
#
#class ReferralExecute(APIView):
#    def get_object(self, theName):
#        try:
#            return Referral.objects.get(name=theName)
#        except Referral.DoesNotExist:
#            raise Http404
#
#    def get(self, request, theName, format=None):
#        referral = self.get_object(theName)
#        serializer = ReferralSerializer(referral)
#        referral.incrementCountNow()
#        return HttpResponseRedirect('/landing/?link=' + theName) 
#        return Response(serializer.data)

@csrf_exempt
def referral_execute(request, theName):
    try:
        referral = Referral.objects.get(name=theName)
    except Referral.DoesNotExist:
        template = loader.get_template('referral/landingPageNotConfigured.html')
        context = RequestContext(request, {
            'name': theName,
        })
        return HttpResponse(template.render(context))

    if request.method == 'GET':
        serializer = ReferralSerializer(referral)
        referral.incrementCountNow()
        return HttpResponseRedirect('/landing/?link=' + theName) 


def landingPage(request):
    template = loader.get_template('referral/landingPage.html')
    return HttpResponse(template.render())


def overviewPage(request):
    referral = Referral.objects.all()
    serializer = ReferralSerializer(referral, many=True)
    referralJsonData = JSONRenderer().render(serializer.data)
    template = loader.get_template('referral/overviewPage.html')
    context = RequestContext(request, {
        'referraljson': referralJsonData,
    })
    return HttpResponse(template.render(context))


