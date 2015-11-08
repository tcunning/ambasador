# 
# ./manage.py makemigrations referral
# ./manage.py migrate
#
from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError

def validate_referral_name(value):
    lowervalue = value.lower()
    if lowervalue == "landing" or lowervalue == "admin":
        raise ValidationError("name can't be %s" % value)

class Referral(models.Model):
    name = models.CharField('name', max_length=200, unique=True, validators=[validate_referral_name])
    count = models.PositiveIntegerField('count')
    
    def __str__(self):
        return self.name + "(" + `self.count` + ")"

    def incrementCountNow(self):
        self.count = F('count') + 1
        self.save()
        self.refresh_from_db()

	def saveName(self):
		super(Referral, self).save(update_fields=['name'])
		

# See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/ for
# how to override save (to do extra work)
