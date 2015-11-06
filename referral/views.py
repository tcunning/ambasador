"""
http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from referral.models import Referral
from referral.serializers import ReferralSerializer

# http://localhost:8000/referral/
#
@api_view(['GET', 'POST'])
def referral_list(request, format=None):
	if request.method == 'GET':
		referral = Referral.objects.all()
		serializer = ReferralSerializer(referral, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = ReferralSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# http://localhost:8000/referral/test/
#
@api_view(['GET', 'PUT', 'DELETE'])
def referral_detail(request, theName, format=None):
	try:
		referral = Referral.objects.get(name=theName)
	except Referral.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ReferralSerializer(referral)
		referral.incrementCountNow()
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ReferralSerializer(referral, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		referral.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)