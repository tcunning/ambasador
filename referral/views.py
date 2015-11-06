from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from referral.models import Referral
from referral.serializers import ReferralSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


"""
List all referral, or create a new referral.

Because we want to be able to POST to this view from clients that won't have a CSRF 
token we need to mark the view as csrf_exempt
"""
@csrf_exempt
def referral_list(request):
	"""
	"""
	if request.method == 'GET':
		referral = Referral.objects.all()
		serializer = ReferralSerializer(referral, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ReferralSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)


"""
Retrieve, update or delete a referral.
"""
@csrf_exempt
def referral_detail(request, theName):
	try:
		referral = Referral.objects.get(name=theName)
	except Referral.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ReferralSerializer(referral)
		referral.incrementCountNow()
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ReferralSerializer(referral, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		referral.delete()
		return HttpResponse(status=204)