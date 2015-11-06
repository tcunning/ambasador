from rest_framework import serializers
from referral.models import Referral

# Simple form for serialize.
# 	See http://www.django-rest-framework.org/api-guide/serializers/  
# 	See http://www.django-rest-framework.org/tutorial/1-serialization/
#
class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = ('id', 'name', 'count')
    
    # Example on how to do validation on update
    #
    #def create(self, validated_data):
    #    profile_data = validated_data.pop('profile')
    #    user = User.objects.create(**validated_data)
    #    Profile.objects.create(user=user, **profile_data)
    #    return user