"""
http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from referral.models import Referral
from referral.serializers import ReferralSerializer

# http://localhost:8000/referral/
#
class ReferralList(APIView):
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

    permission_classes = (permissions.AllowAny,)

# http://localhost:8000/referral/test/
#
class ReferralDetail(APIView):
    def get_object(self, theName):
        try:
            return Referral.objects.get(name=theName)
        except Referral.DoesNotExist:
            raise Http404

    def get(self, request, theName, format=None):
        referral = self.get_object(theName)
        serializer = ReferralSerializer(referral)
        referral.incrementCountNow()
        return Response(serializer.data)

    def put(self, request, theName, format=None):
        referral = self.get_object(theName)
        serializer = ReferralSerializer(referral, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, theName, format=None):
        referral = self.get_object(theName)
        referral.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = (permissions.AllowAny,)
